# labels: test_group::mlagility name::retinanet_resnet50_fpn author::torchvision
"""
https://pytorch.org/vision/stable/models/retinanet.html
"""

import mlagility
import torch
from torchvision.models.detection import retinanet_resnet50_fpn


torch.manual_seed(0)

# Parsing command-line arguments
batch_size, num_channels, width, height = mlagility.parse(
    ["batch_size", "num_channels", "width", "height"]
)


# Model and input configurations
model = retinanet_resnet50_fpn()
model.eval()
inputs = {"images": torch.ones([batch_size, num_channels, width, height])}


# Call model
model(**inputs)
