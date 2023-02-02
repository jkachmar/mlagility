# labels: test_group::mlagility name::microsoft_swin_tiny_patch4_window7_224 author::huggingface_tf
"""
https://huggingface.co/microsoft/swin-tiny-patch4-window7-224
"""

import mlagility
import transformers
import tensorflow as tf

tf.random.set_seed(0)

# Parsing command-line arguments
batch_size, max_seq_length = mlagility.parse(["batch_size", "max_seq_length"])


config = transformers.AutoConfig.from_pretrained(
    "microsoft/swin-tiny-patch4-window7-224"
)
model = transformers.TFAutoModel.from_config(config)
inputs = {
    "input_ids": tf.ones(shape=(batch_size, max_seq_length), dtype=tf.int32),
}

model(**inputs)


# Call model
model(**inputs)
