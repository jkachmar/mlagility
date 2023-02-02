# labels: test_group::mlagility name::squeezenet1_1 author::torch_hub_vision
"""
https://github.com/pytorch/hub/blob/master/pytorch_vision_squeezenet.md
"""

from mlagility.parser import parse
import torch

torch.manual_seed(0)

# Parsing command-line arguments
batch_size, num_channels, width, height = parse(
    ["batch_size", "num_channels", "width", "height"]
)


# Model and input configurations
model = torch.hub.load(
    "pytorch/vision:v0.13.1",
    "squeezenet1_1",
    weights=None,
)
model.eval()
inputs = {"x": torch.ones([batch_size, num_channels, width, height])}


# Call model
model(**inputs)
