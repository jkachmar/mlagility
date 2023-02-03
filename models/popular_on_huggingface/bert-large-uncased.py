# labels: test_group::monthly author::huggingface name::bert-large-uncased downloads::1,069,047 license::apache-2.0 task::Fill-Mask
from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-large-uncased')
unmasker("Hello I'm a [MASK] model.")

