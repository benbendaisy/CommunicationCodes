# pip install transformers faiss-cpu datasets

import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
from transformers import BartTokenizer, BartForConditionalGeneration


"""

Components of a RAG System:

1, Document Indexing: Convert a corpus into embeddings and store it in a searchable index.

2, Retriever: Given a query, retrieve top-K most relevant documents.

3, Generator: Use a generative model to synthesize an answer conditioned on the query and retrieved documents.

"""


"""
Index all the documents
"""
# Sample corpus
documents = [
    "The Eiffel Tower is located in Paris.",
    "The Great Wall of China is visible from space.",
    "Python is a popular programming language.",
]

# Embed the documents using a sentence transformer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def embed(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        model_output = model(**inputs)
    return model_output.last_hidden_state[:, 0, :].cpu().numpy()

doc_embeddings = embed(documents)

# Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)


"""
Retrieve top k documents
"""
def retrieve(query, k=2):
    query_embedding = embed([query])
    distances, indices = index.search(query_embedding, k)
    return [documents[i] for i in indices[0]]


"""
Generate the syntheisized results
"""
gen_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large")
gen_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large")

def generate_answer(query, k=2):
    retrieved_docs = retrieve(query, k)
    inputs = [f"Context: {doc} Question: {query}" for doc in retrieved_docs]
    tokenized_inputs = gen_tokenizer(inputs, return_tensors="pt", padding=True, truncation=True)
    
    with torch.no_grad():
        output_ids = gen_model.generate(**tokenized_inputs, max_length=50)
    
    return [gen_tokenizer.decode(output, skip_special_tokens=True) for output in output_ids]


"""
Example usage
"""
query = "Where is the Eiffel Tower?"
answers = generate_answer(query)
print(answers)