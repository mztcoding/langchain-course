# RAG Architecture:

Now, its time to learn about RAG.

*RAG stands for Retrieval-Augmented Generation. It's an architecture designed to combine the strengths of information retrieval systems and generative models (llms), specifically in the context of NLP tasks.*

Now, let's elaborate this definition and understand what these
terms, Retrieval, Augmented and Generation, mean? and understand the RAG pipeline.

## Components in RAG architecture:

**Corpus or Knowledge Base:** The source of documents and information for retrieval.

**Document Encoder:** Encodes the documents into vectors.

**Vector Database:** A database where the encoded documents are stored in the form of vectors.

**Query Encoder:** Encodes the input query into a vector representation.

**Retriever:** Searches and retrieves relevant documents based on the encoded query.

**Chains:** Combines the query and document embeddings.

**Generative Model:** Generates the final response using the combined embeddings.

## RAG pipeline in steps:

**1.** First of all, corpus or knowledge base is taken and converted into vectors/embeddings by using some text embedding model. These embeddings are then stored in a vector database. 

**2.** The pipeline starts with an input query, which could be a question, a prompt, or any text requiring a response. The query is then encoded into vector representation.

**3.** Retrieval is the process of locating and obtaining relevant data or documents from a database or vector store using a specified query or input. When user enters a prompt, the retriever searches for the relevant information in the vector database where the embeddings are stored.

**4.** The encoded query and the encoded documents are combined to form a single input for the generative model. The combined input is fed into a generative model, such as GPT, which generates a coherent and contextually relevant response.