# labels: test_group::mlagility name::electra_for_sequence_classification author::transformers
from mlagility.parser import parse
import transformers
import torch

# Parsing command-line arguments
batch_size, max_seq_length = parse(["batch_size", "max_seq_length"])


# This version of Electra performs sequence classification,
# while the default model outputs raw hidden states.

# Model and input configurations
model = transformers.ElectraForSequenceClassification.from_pretrained(
    "howey/electra-base-sst2"
)
inputs = {
    "input_ids": torch.ones(batch_size, max_seq_length, dtype=torch.long),
    "attention_mask": torch.ones(batch_size, max_seq_length, dtype=torch.float),
}


# Call model
model(**inputs)
