import time
import os
import json
import pathlib
from typing import Tuple, List
import groqflow.common.printing as printing
import groqflow.common.exceptions as exceptions
import groqflow.common.build
import mlagility.slurm as slurm
import mlagility.filesystem as filesystem
from mlagility.analysis.analysis import evaluate_script, TracerArgs, Action


def decode_script_name(input: str) -> Tuple[str, List[str]]:
    # Parse the targets out of the script name
    # Targets use the format:
    #   script_name.py:target0,target1,...,targetN
    decoded_name = input.split(":")
    script_name = decoded_name[0]

    if len(decoded_name) == 2:
        targets = decoded_name[1].split(",")
    elif len(decoded_name) == 1:
        targets = []
    else:
        raise ValueError(
            "Each script input to benchit should have either 0 or 1 ':' in it."
            f"However, {script_name} was received."
        )

    return script_name, targets


def main(args):

    # Force the user to specify a legal cache dir in NFS if they are using slurm
    if not os.path.expanduser(args.cache_dir).startswith("/net") and args.use_slurm:
        raise ValueError(
            "You must specify a --cache-dir in `/net` when using groqit-util with Slurm, "
            f"however your current --cache-dir is set to {os.path.expanduser(args.cache_dir)}"
        )

    # Get a specific list of models to process
    available_scripts = filesystem.get_available_scripts(args.search_dir)

    # Filter based on the model names provided by the user
    if args.input_scripts == ["all"]:
        scripts = [
            os.path.join(args.search_dir, script) for script in available_scripts
        ]
    else:
        scripts = []
        for user_script in args.input_scripts:
            user_script_path = os.path.join(args.search_dir, user_script)

            # Ignore everything after the ':' symbol, if there is one
            clean_user_script_path = user_script_path.split(":")[0]

            # Validate that the script exists
            if os.path.exists(clean_user_script_path):
                scripts.append(user_script_path)
            else:
                raise exceptions.GroqitArgError(
                    f"Script could not be found: {user_script_path}"
                )

    # Decode benchit args into TracerArgs flags
    if args.analyze_only:
        actions = [
            Action.ANALYZE,
        ]
    elif args.build_only:
        actions = [
            Action.ANALYZE,
            Action.BUILD,
        ]
    else:
        actions = [
            Action.ANALYZE,
            Action.BUILD,
            Action.BENCHMARK,
        ]

    if args.use_slurm:
        jobs = slurm.jobs_in_queue()
        if len(jobs) > 0:
            printing.log_warning(f"There are already slurm jobs in your queue: {jobs}")
            printing.log_info(
                "Suggest quitting benchit, running 'scancel -u $USER' and trying again."
            )

    for script in scripts:
        for device in args.devices:
            if args.use_slurm:
                slurm.run_benchit(
                    op="benchmark",
                    script=script,
                    search_dir=args.search_dir,
                    cache_dir=args.cache_dir,
                    rebuild=args.rebuild,
                    compiler_flags=args.compiler_flags,
                    assembler_flags=args.assembler_flags,
                    num_chips=args.num_chips,
                    groqview=args.groqview,
                    devices=device,
                    runtimes=args.runtimes,
                    ip=args.ip,
                    max_depth=args.max_depth,
                    analyze_only=args.analyze_only,
                    build_only=args.build_only,
                )

            else:

                # Parse the targets out of the script name
                script_name, targets = decode_script_name(script)

                # Instantiate an object that holds all of the arguments
                # for analysis, build, and benchmarking
                tracer_args = TracerArgs(
                    input=script_name,
                    lean_cache=args.lean_cache,
                    targets=targets,
                    max_depth=args.max_depth,
                    cache_dir=args.cache_dir,
                    rebuild=args.rebuild,
                    compiler_flags=args.compiler_flags,
                    assembler_flags=args.assembler_flags,
                    num_chips=args.num_chips,
                    groqview=args.groqview,
                    device=device,
                    actions=actions,
                )

                # Run analysis, build, and benchmarking on every model
                # in the script
                evaluate_script(tracer_args, args.script_args)

                # Print performance info
                if args.devices and Action.BENCHMARK in actions:
                    builds = filesystem.get_builds_from_script(
                        args.cache_dir, pathlib.Path(script).stem
                    )
                    for build in builds:
                        if "x86" in args.devices:
                            perf_file = os.path.join(
                                groqflow.common.build.output_dir(args.cache_dir, build),
                                "cpu_performance.json",
                            )
                            with open(perf_file, "r", encoding="utf8") as stream:
                                perf_data = json.loads(stream.read())
                                printing.log_info(
                                    f"Performance of device {perf_data['CPU Name']} is:"
                                )
                                print(f"Latency: {perf_data['Mean Latency(ms)']} ms")
                                print(f"Throughput: {perf_data['Throughput']} IPS")

    # Wait until all the Slurm jobs are done
    if args.use_slurm:
        while len(slurm.jobs_in_queue()) != 0:
            print(
                f"Waiting: {len(slurm.jobs_in_queue())} "
                f"jobs left in queue: {slurm.jobs_in_queue()}"
            )
            time.sleep(5)

    printing.log_success(
        "The 'benchmark' command is complete. Use the 'report' command to get a .csv "
        "file that summarizes results across all builds in the cache."
    )
