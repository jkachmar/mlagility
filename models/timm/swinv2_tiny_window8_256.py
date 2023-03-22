# labels: test_group::mlagility name::swinv2_tiny_window8_256 author::timm
import torch
import timm
from mlagility.parser import parse

# Parsing command-line arguments
batch_size = parse(["batch_size"])

# Creating model
model = timm.create_model("swinv2_tiny_window8_256", pretrained = False)

# Creating inputs
input_size = model.default_cfg["input_size"]
batched_input_size = tuple(batch_size) + input_size
inputs = torch.rand(batched_input_size)

# Calling model
model(inputs)
