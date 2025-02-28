from backend.api.rag_pipeline import retrieve_relevant_docs

def handle_query(question):
    docs = retrieve_relevant_docs(question)
    
    if not docs:
        return {"response": "Sorry, I couldn't find relevant information."}
    
    response = "\n".join([f"{doc['cdp']}: {doc['text']}" for doc in docs])
    return {"response": response}
