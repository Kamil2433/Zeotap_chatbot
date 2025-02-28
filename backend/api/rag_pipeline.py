import pickle
import faiss
import os
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer('all-MiniLM-L6-v2')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
VECTOR_STORE_PATH = os.path.join(BASE_DIR, "..", "data_ingestion", "vector_store.pkl")

with open(VECTOR_STORE_PATH, "rb") as f:
    INDEX, TEXT_MAP = pickle.load(f)

def retrieve_relevant_docs(query):
    query_vector = MODEL.encode([query], convert_to_numpy=True)
    D, I = INDEX.search(query_vector, k=3)

    results = [TEXT_MAP[idx] for idx in I[0] if idx in TEXT_MAP]
    return results
