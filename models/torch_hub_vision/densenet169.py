# labels: test_group::mlagility name::densenet169 author::torch_hub_vision
"""
https://github.com/pytorch/hub/blob/master/pytorch_vision_densenet.md
"""

import mlagility
import torch

torch.manual_seed(0)

# Parsing command-line arguments
batch_size, num_channels, width, height = mlagility.parse(
    ["batch_size", "num_channels", "width", "height"]
)


# Model and input configurations
model = torch.hub.load(
    "pytorch/vision:v0.13.1",
    "densenet169",
    weights=None,
)
model.eval()
inputs = {"x": torch.ones([batch_size, num_channels, width, height])}


# Call model
model(**inputs)
