# labels: test_group::mlagility name::xcit_nano_12_p8_224_dist author::timm
import torch
import timm
from mlagility.parser import parse

# Parsing command-line arguments
batch_size = parse(["batch_size"])

# Creating model
model = timm.create_model("xcit_nano_12_p8_224_dist", pretrained = False)

# Creating inputs
input_size = model.default_cfg["input_size"]
batched_input_size = tuple(batch_size) + input_size
inputs = torch.rand(batched_input_size)

# Calling model
model(inputs)
