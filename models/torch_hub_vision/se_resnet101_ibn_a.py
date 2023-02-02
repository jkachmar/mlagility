# labels: test_group::mlagility name::se_resnet101_ibn_a author::torch_hub_vision
"""
https://github.com/pytorch/hub/blob/master/pytorch_vision_ibnnet.md
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
    "XingangPan/IBN-Net",
    "se_resnet101_ibn_a",
    weights=None,
)
model.eval()
inputs = {"x": torch.ones([batch_size, num_channels, width, height])}


# Call model
model(**inputs)
