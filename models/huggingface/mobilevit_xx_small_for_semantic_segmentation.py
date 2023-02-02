# labels: test_group::mlagility name::mobilevit_xx_small_for_semantic_segmentation author::huggingface
"""https://huggingface.co/apple/mobilevit-xx-small"""
import mlagility
import transformers
import torch

# Parsing command-line arguments
batch_size, height, num_channels, width = mlagility.parse(
    ["batch_size", "height", "num_channels", "width"]
)


# Model and input configurations
model = transformers.MobileViTForSemanticSegmentation.from_pretrained(
    "apple/deeplabv3-mobilevit-xx-small"
)

inputs = {
    "pixel_values": torch.ones(
        batch_size, num_channels, height, width, dtype=torch.float
    ),
}


# Call model
model(**inputs)
