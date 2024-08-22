import streamlit as st
import os
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS


# We are using HuggingFace Embeddings for better results.
embeddings = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device':'cpu'},
    encode_kwargs={'normalize_embeddings':True}
)
vectors = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
st.title("Your assistant chatbot")
llm = Ollama(model="llama3.1")

prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)
document_chain = create_stuff_documents_chain(llm, prompt)
retriever = vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

txt=st.text_input("Input you question here")

if txt:
    
    response=retrieval_chain.invoke({"input":txt})
    st.write(response['answer'])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")