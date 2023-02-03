# labels: test_group::monthly author::sentence-transformers name::xlm-r-bert-base-nli-stsb-mean-tokens downloads::651 license::apache-2.0 task::Sentence_Similarity
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/xlm-r-bert-base-nli-stsb-mean-tokens')
embeddings = model.encode(sentences)
print(embeddings)
