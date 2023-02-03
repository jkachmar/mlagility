# labels: test_group::monthly author::sentence-transformers name::roberta-base-nli-mean-tokens downloads::1,225 license::apache-2.0 task::Sentence_Similarity
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/roberta-base-nli-mean-tokens')
embeddings = model.encode(sentences)
print(embeddings)
