# labels: test_group::mlagility name::xlnet-512 author::huggingface
import mlagility
import transformers
import torch

torch.manual_seed(0)

# Parsing command-line arguments
batch_size = mlagility.parse(["batch_size"])


# Model and input configurations
config = transformers.XLNetConfig()
model = transformers.XLNetModel(config)
inputs = {
    "input_ids": torch.ones(batch_size, 512, dtype=torch.long),
    "attention_mask": torch.ones(batch_size, 512, dtype=torch.float),
}


# Call model
model(**inputs)
