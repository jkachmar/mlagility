# labels: test_group::mlagility name::vit_base_r50_s16_224_in21k author::timm
import torch
import timm
from mlagility.parser import parse

# Parsing command-line arguments
batch_size = parse(["batch_size"])

# Creating model
model = timm.create_model("vit_base_r50_s16_224_in21k", pretrained = False)

# Creating inputs
input_size = model.default_cfg["input_size"]
batched_input_size = tuple(batch_size) + input_size
inputs = torch.rand(batched_input_size)

# Calling model
model(inputs)
