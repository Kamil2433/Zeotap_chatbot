def rank_results(docs):
    return sorted(docs, key=lambda x: len(x["text"]), reverse=True)
