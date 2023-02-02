# labels: test_group::mlagility name::midas_v2.1_small author::torch_hub
"""https://pytorch.org/hub/intelisl_midas_v2/"""
import mlagility
import torch

torch.manual_seed(0)

# Parsing command-line arguments
batch_size, height, num_channels, width = mlagility.parse(
    ["batch_size", "height", "num_channels", "width"]
)


# Model and input configurations
model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")

inputs = {"x": torch.ones(batch_size, num_channels, height, width, dtype=torch.float)}


# Call model
model(**inputs)
