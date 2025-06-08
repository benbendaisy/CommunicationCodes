import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from sentence_transformers import SentenceTransformer, util
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. Knowledge Graph Component ---
class KnowledgeGraph:
    def __init__(self):
        self.triples = []
        self.entities = set()
        self._initialize_sample_kg()

    def _initialize_sample_kg(self):
        self.add_triple("PyTorch", "is_a", "Machine Learning Library")
        self.add_triple("PyTorch", "developed_by", "Meta AI")
        self.add_triple("PyTorch", "used_for", "Deep Learning")
        self.add_triple("RAG", "stands_for", "Retrieval Augmented Generation")
        self.add_triple("RAG", "improves", "Large Language Models")
        self.add_triple("Knowledge Graph", "stores", "structured data")
        self.add_triple("Knowledge Graph", "represents", "entities and relationships")
        self.add_triple("PrismaticAI", "focuses_on", "GraphRAG") # Example entity

    def add_triple(self, subject, predicate, obj):
        self.triples.append((subject, predicate, obj))
        self.entities.add(subject)
        self.entities.add(obj) # Add object as potential entity too

    def get_facts_about_entity(self, entity_name):
        facts = []
        for s, p, o in self.triples:
            if s.lower() == entity_name.lower():
                facts.append((s, p, o))
            elif o.lower() == entity_name.lower(): # Also find facts where entity is an object
                facts.append((s, p, o))
        return facts

    def textualize_facts(self, facts):
        if not facts:
            return "No specific facts found in the Knowledge Graph."
        return " ".join([f"{s} {p.replace('_', ' ')} {o}." for s, p, o in facts])

# --- 2. Document Retriever Component ---
class DocumentRetriever:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.doc_embeddings = None
        self._initialize_sample_documents()

    def _initialize_sample_documents(self):
        self.add_document(
            "PyTorch is an open-source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing. It is primarily developed by Facebook's AI Research lab (FAIR)."
        )
        self.add_document(
            "Retrieval Augmented Generation (RAG) is a technique for improving the accuracy and reliability of Large Language Models (LLMs) by providing them with external knowledge from documents or databases during the generation process."
        )
        self.add_document(
            "Knowledge Graphs are structured representations of facts, consisting of entities, relationships, and semantic descriptions. They are used to connect disparate information and enable more effective data integration and discovery."
        )
        self.add_document(
            "GraphRAG combines the strengths of Knowledge Graphs for structured data and RAG for unstructured text, aiming to provide LLMs with comprehensive and contextually rich information for generation."
        )
        self.add_document(
            "PrismaticAI is developing advanced solutions using Knowledge Graphs and Large Language Models to solve complex enterprise problems through enhanced understanding and reasoning."
        )
        self.encode_documents()


    def add_document(self, text):
        self.documents.append(text)

    def encode_documents(self):
        if self.documents:
            self.doc_embeddings = self.model.encode(self.documents, convert_to_tensor=True)
        else:
            self.doc_embeddings = torch.empty(0)


    def retrieve(self, query, top_k=2):
        if not self.documents or self.doc_embeddings is None or self.doc_embeddings.nelement() == 0:
            return []
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        
        # For newer sentence-transformers, util.pytorch_cos_sim is preferred
        # For older or if you want to use sklearn
        # cos_scores = util.pytorch_cos_sim(query_embedding, self.doc_embeddings)[0]
        
        # Using sklearn for broader compatibility if util.pytorch_cos_sim causes issues in some setups
        # Ensure embeddings are on CPU and are numpy arrays for sklearn
        query_emb_np = query_embedding.cpu().numpy().reshape(1, -1)
        doc_embs_np = self.doc_embeddings.cpu().numpy()
        
        if doc_embs_np.shape[0] == 0: # No documents
             return []

        cos_scores = cosine_similarity(query_emb_np, doc_embs_np)[0]
        
        # Get top_k scores and their indices
        # Using torch for sorting if we stuck with PyTorch tensors for scores
        # top_results = torch.topk(cos_scores, k=min(top_k, len(self.documents)))
        # indices = top_results.indices.tolist()
        
        # Using numpy for sorting with sklearn's cosine_similarity output
        top_k_indices = np.argsort(cos_scores)[-top_k:][::-1].tolist()
        
        return [self.documents[idx] for idx in top_k_indices if cos_scores[idx] > 0.3] # Add a relevance threshold

# --- 3. Generator Component ---
class Generator:
    def __init__(self, model_name='t5-small'):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate(self, prompt_text, max_length=150):
        inputs = self.tokenizer("summarize: " + prompt_text, return_tensors="pt", max_length=1024, truncation=True).to(self.device)
        # Note: "summarize: " prefix is often used for T5 for summarization/QnA tasks.
        # You might need to adjust or remove it depending on fine-tuning or base model behavior.

        summary_ids = self.model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_length=max_length,
            num_beams=4, # You can experiment with beam search
            early_stopping=True
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# --- 4. GraphRAG System ---
class GraphRAGSystem:
    def __init__(self):
        self.kg = KnowledgeGraph()
        self.retriever = DocumentRetriever()
        self.generator = Generator()

    def _simple_entity_linker(self, query):
        # Very basic entity linking: exact match (case-insensitive) of known KG entities
        linked_entities = []
        # Split query into words, also consider multi-word entities by checking substrings
        # For this sample, we'll just iterate through known KG entities
        for entity in self.kg.entities:
            if entity.lower() in query.lower():
                linked_entities.append(entity)
        return list(set(linked_entities)) # Unique entities

    def answer_query(self, query):
        print(f"🔍 Query: {query}\n")

        # 1. Query Understanding (Simplified Entity Linking)
        linked_entities = self._simple_entity_linker(query)
        print(f"🔗 Linked Entities in KG: {linked_entities if linked_entities else 'None'}")

        # 2. KG Retrieval
        kg_facts_text = ""
        if linked_entities:
            all_facts = []
            for entity in linked_entities:
                facts = self.kg.get_facts_about_entity(entity)
                all_facts.extend(facts)
            # Remove duplicate facts if an entity was linked multiple times or facts overlap
            unique_facts = sorted(list(set(all_facts)))
            kg_facts_text = self.kg.textualize_facts(unique_facts)
        else:
            kg_facts_text = "No specific entities from the query were directly found in the Knowledge Graph."
        
        print(f"\n🧠 Knowledge Graph Context:\n{kg_facts_text}\n")

        # 3. Document Retrieval (RAG)
        retrieved_docs = self.retriever.retrieve(query, top_k=2)
        retrieved_docs_text = "\n".join([f"Document {i+1}: {doc}" for i, doc in enumerate(retrieved_docs)])
        if not retrieved_docs:
            retrieved_docs_text = "No relevant documents found."
        
        print(f"📚 Retrieved Documents Context:\n{retrieved_docs_text}\n")

        # 4. Context Combination
        # We can be more sophisticated here, but for a sample, simple concatenation is fine.
        combined_context = f"Based on the following information, answer the query.\n"
        combined_context += f"Knowledge Graph Information: {kg_facts_text}\n"
        combined_context += f"Retrieved Documents: {retrieved_docs_text}\n\n"
        
        prompt_for_generator = f"Query: {query}\n\nContext:\n{combined_context}Answer:"
        
        # 5. Generation
        print("⏳ Generating answer...")
        answer = self.generator.generate(prompt_for_generator)
        
        print(f"\n💡 Generated Answer:\n{answer}")
        return answer

# --- Example Usage ---
if __name__ == "__main__":
    system = GraphRAGSystem()

    print("\n--- Example 1 ---")
    query1 = "Tell me about PyTorch."
    system.answer_query(query1)

    print("\n--- Example 2 ---")
    query2 = "What is RAG and how does it relate to Knowledge Graphs?"
    system.answer_query(query2)
    
    print("\n--- Example 3 ---")
    query3 = "What is PrismaticAI working on?"
    system.answer_query(query3)

    print("\n--- Example 4 (Entity not strongly in KG/Docs) ---")
    query4 = "What is the capital of France?" # This query has less direct support in our tiny KG/docs
    system.answer_query(query4)