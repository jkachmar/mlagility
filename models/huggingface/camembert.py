# labels: test_group::mlagility name::camembert author::huggingface
import mlagility
import transformers
import torch

torch.manual_seed(0)

# Parsing command-line arguments
batch_size, max_seq_length = mlagility.parse(["batch_size", "max_seq_length"])


# Model and input configurations
config = transformers.CamembertConfig()
model = transformers.CamembertModel(config)
inputs = {
    "input_ids": torch.ones(batch_size, max_seq_length, dtype=torch.long),
    "attention_mask": torch.ones(batch_size, max_seq_length, dtype=torch.float),
}


# Call model
model(**inputs)
