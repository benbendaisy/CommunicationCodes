# pip install transformers sentence-transformers rdflib faiss-cpu networkx


import networkx as nx

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import BartTokenizer, BartForConditionalGeneration

"""
We'll implement the following:

1, Knowledge Graph Construction: Convert documents into a graph of triples (subject, predicate, object).

2, KG Indexing + Retrieval: Given a query, use entity linking and graph search to find relevant nodes and subgraphs.

3, Document Retrieval: Use the KG context to retrieve relevant textual documents.

4, Answer Generation: Combine the query and retrieved content and pass it to a generative model (e.g., BART).

"""

"""
Step 1: Building knowledge graph
"""
# Triples: (subject, relation, object)
triples = [
    ("Eiffel Tower", "located_in", "Paris"),
    ("Great Wall of China", "located_in", "China"),
    ("Python", "is_a", "Programming Language"),
]

# Create directed graph
G = nx.DiGraph()
for s, p, o in triples:
    G.add_edge(s, o, relation=p)

def query_kg(entity):
    # Return connected neighbors and their relation
    neighbors = G[entity] if entity in G else {}
    return [(entity, G[entity][n]['relation'], n) for n in neighbors]



"""
Step 2: Document indexing with FAISS
"""

model = SentenceTransformer("all-MiniLM-L6-v2")

entity_docs = {
    "Eiffel Tower": "The Eiffel Tower is an iron tower located in Paris.",
    "Paris": "Paris is the capital of France.",
    "Python": "Python is a high-level programming language.",
    "Programming Language": "Programming languages allow communication with computers.",
    "Great Wall of China": "The Great Wall of China is a historic fortification in China.",
    "China": "China is a country in East Asia.",
}

entities = list(entity_docs.keys())
doc_texts = list(entity_docs.values())
embeddings = model.encode(doc_texts, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


"""
Step 3: Graph-Aided retrieval
"""

def retrieve_from_kg_and_docs(query, k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)
    D, I = index.search(query_embedding, k)
    results = [entities[i] for i in I[0]]
    
    # Expand via KG
    expanded = set()
    for ent in results:
        expanded.add(ent)
        for _, _, neighbor in query_kg(ent):
            expanded.add(neighbor)
    
    return list(expanded), [entity_docs[e] for e in expanded if e in entity_docs]


"""
Step 4: RAG-style generation
"""
gen_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large")

def generate_answer_with_kg(query):
    entities, texts = retrieve_from_kg_and_docs(query)
    context = " ".join(texts)
    prompt = f"Context: {context} Question: {query}"
    
    inputs = tokenizer([prompt], return_tensors="pt", truncation=True)
    output = gen_model.generate(**inputs, max_length=64)
    return tokenizer.decode(output[0], skip_special_tokens=True)


"""
Example Usage
"""
query = "Where is the Eiffel Tower?"
print(generate_answer_with_kg(query))