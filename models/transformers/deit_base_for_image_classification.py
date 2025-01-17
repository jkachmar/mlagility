# labels: test_group::mlagility name::deit_base_for_image_classification author::transformers
"""https://huggingface.co/facebook/deit-base-patch16-224"""
from mlagility.parser import parse
import transformers
import torch

# Parsing command-line arguments
batch_size, height, num_channels, width = parse(
    ["batch_size", "height", "num_channels", "width"]
)


# Model and input configurations
model = transformers.ViTForImageClassification.from_pretrained(
    "facebook/deit-base-patch16-224"
)
inputs = {
    "pixel_values": torch.ones(
        batch_size, num_channels, height, width, dtype=torch.float
    ),
}


# Call model
model(**inputs)
