# labels: name::vilt author::skip
import mlagility
import transformers
import torch

# Parsing command-line arguments
batch_size, height, num_channels, width = mlagility.parse(
    ["batch_size", "height", "num_channels", "width"]
)


# Model and input configurations
config = transformers.ViltConfig()
model = transformers.ViltModel(config)
inputs = {
    "input_ids": torch.ones(batch_size, 40, dtype=torch.long),
    "pixel_values": torch.ones(
        batch_size, num_channels, height, width, dtype=torch.float
    ),
}


# Call model
model(**inputs)
