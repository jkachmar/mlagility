# labels: test_group::mlagility name::fasterrcnn_resnet50_fpn author::torchvision
"""
https://pytorch.org/vision/stable/models/faster_rcnn.html
"""

import mlagility
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn


torch.manual_seed(0)

# Parsing command-line arguments
batch_size, num_channels, width, height = mlagility.parse(
    ["batch_size", "num_channels", "width", "height"]
)


# Model and input configurations
model = fasterrcnn_resnet50_fpn()
model.eval()
inputs = {"images": torch.ones([batch_size, num_channels, width, height])}


# Call model
model(**inputs)
