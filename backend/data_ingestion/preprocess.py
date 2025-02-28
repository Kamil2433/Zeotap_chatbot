import json
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
import time
from tqdm import tqdm

# Load the model
print("🔄 Loading sentence transformer model...")
MODEL = SentenceTransformer('all-MiniLM-L6-v2')
print("✅ Model loaded successfully.\n")

def load_data():
    print("📂 Loading data from cdp_docs.json...")
    time.sleep(1)
    with open("scraped_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"✅ Loaded {len(data)} documents.\n")
    return data  # Expecting a list of dictionaries

def create_embeddings(data):
    text_data = []
    text_map = {}

    print("📊 Splitting text into chunks and processing links...")
    time.sleep(1)

    index = 0
    for doc_index, entry in tqdm(enumerate(data), desc="Processing CDP Docs"):
        cdp = entry.get("url", f"Document-{doc_index}")  # Use URL as identifier
        content = entry.get("content", "")
        links = entry.get("links", [])  # Extract links

        # Split content into sentences
        chunks = content.split(". ")
        for chunk in chunks:
            if chunk.strip():  # Ignore empty chunks
                text_data.append(chunk)
                text_map[index] = {"cdp": cdp, "text": chunk, "links": links}
                index += 1

    print("\n🧠 Generating embeddings. This may take a moment...")
    embeddings = MODEL.encode(text_data, convert_to_numpy=True)

    print("📌 Creating FAISS index...")
    faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
    faiss_index.add(embeddings)

    print("💾 Saving embeddings to vector_store.pkl...")
    with open("vector_store.pkl", "wb") as f:
        pickle.dump((faiss_index, text_map), f)

    print("\n✅ Embeddings and links saved successfully.")

if __name__ == "__main__":
    data = load_data()
    create_embeddings(data)
