from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
import os
import shutil

FAISS_PATH = "faiss_index"
DATA_PATH = "UG_Prospectus_2023.pdf"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_faiss(chunks)


def load_documents():
    loader = PyPDFLoader(DATA_PATH)
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_faiss(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(FAISS_PATH):
        shutil.rmtree(FAISS_PATH)

    # Create a new DB from the documents.
    embeddings = HuggingFaceBgeEmbeddings(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={'device':'cpu'},
        encode_kwargs={'normalize_embeddings':True}
    )
    db = FAISS.from_documents(
        chunks, embeddings
    )
    db.save_local("faiss_index")
    print(f"Saved {len(chunks)} chunks to {FAISS_PATH}.")


if __name__ == "__main__":
    main()