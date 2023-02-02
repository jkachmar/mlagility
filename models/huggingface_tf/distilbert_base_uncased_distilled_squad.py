# labels: test_group::mlagility name::distilbert_base_uncased_distilled_squad author::huggingface_tf
"""
https://huggingface.co/distilbert-base-uncased-distilled-squad
"""

from mlagility.parser import parse
import transformers
import tensorflow as tf

tf.random.set_seed(0)

# Parsing command-line arguments
batch_size, max_seq_length = parse(["batch_size", "max_seq_length"])


config = transformers.AutoConfig.from_pretrained(
    "distilbert-base-uncased-distilled-squad"
)
model = transformers.TFAutoModel.from_config(config)
inputs = {
    "input_ids": tf.ones(shape=(batch_size, max_seq_length), dtype=tf.int32),
}

model(**inputs)


# Call model
model(**inputs)
