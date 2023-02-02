# labels: test_group::mlagility name::ssdlite320_mobilenet_v3_large author::torchvision
"""
https://pytorch.org/vision/stable/models/ssdlite.html
"""

import mlagility
import torch
from torchvision.models.detection import ssdlite320_mobilenet_v3_large


torch.manual_seed(0)

# Parsing command-line arguments
batch_size, num_channels, width, height = mlagility.parse(
    ["batch_size", "num_channels", "width", "height"]
)


# Model and input configurations
model = ssdlite320_mobilenet_v3_large()
model.eval()
inputs = {"images": torch.ones([batch_size, num_channels, width, height])}


# Call model
model(**inputs)
