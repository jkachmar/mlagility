# labels: test_group::mlagility name::nvidia_segformer_b0_finetuned_ade_512_512 author::huggingface_tf
"""
https://huggingface.co/nvidia/segformer-b0-finetuned-ade-512-512
"""

import mlagility
import transformers
import tensorflow as tf

tf.random.set_seed(0)

# Parsing command-line arguments
batch_size, max_seq_length = mlagility.parse(["batch_size", "max_seq_length"])


config = transformers.AutoConfig.from_pretrained(
    "nvidia/segformer-b0-finetuned-ade-512-512"
)
model = transformers.TFAutoModel.from_config(config)
inputs = {
    "input_ids": tf.ones(shape=(batch_size, max_seq_length), dtype=tf.int32),
}

model(**inputs)


# Call model
model(**inputs)
