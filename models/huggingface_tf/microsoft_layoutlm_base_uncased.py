# labels: test_group::mlagility name::microsoft_layoutlm_base_uncased author::huggingface_tf
"""
https://huggingface.co/microsoft/layoutlm-base-uncased
"""

import mlagility
import transformers
import tensorflow as tf

tf.random.set_seed(0)

# Parsing command-line arguments
batch_size, max_seq_length = mlagility.parse(["batch_size", "max_seq_length"])


config = transformers.AutoConfig.from_pretrained("microsoft/layoutlm-base-uncased")
model = transformers.TFAutoModel.from_config(config)
inputs = {
    "input_ids": tf.ones(shape=(batch_size, max_seq_length), dtype=tf.int32),
}

model(**inputs)


# Call model
model(**inputs)
