# labels: test_group::mlagility name::mobilevit author::huggingface
"""https://huggingface.co/docs/transformers/model_doc/mobilevit"""
import mlagility
import transformers
import torch

torch.manual_seed(0)

# Parsing command-line arguments
batch_size, height, num_channels, width = mlagility.parse(
    ["batch_size", "height", "num_channels", "width"]
)


# Model and input configurations
config = transformers.MobileViTConfig()
model = transformers.MobileViTModel(config)

inputs = {
    "pixel_values": torch.ones(
        batch_size, num_channels, height, width, dtype=torch.float
    ),
}


# Call model
model(**inputs)
