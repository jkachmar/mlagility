# labels: test_group::mlagility name::sew author::huggingface
import mlagility
import transformers
import torch

torch.manual_seed(0)

# Parsing command-line arguments
batch_size = mlagility.parse(["batch_size"])


# Model and input configurations
config = transformers.SEWConfig()
model = transformers.SEWModel(config)
inputs = {
    "input_values": torch.ones(batch_size, 10000, dtype=torch.float),
}


# Call model
model(**inputs)
