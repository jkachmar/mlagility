# labels: test_group::monthly author::sentence-transformers name::msmarco-distilbert-base-v2 downloads::7,811 license::apache-2.0 task::Sentence_Similarity
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/msmarco-distilbert-base-v2')
embeddings = model.encode(sentences)
print(embeddings)
