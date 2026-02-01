from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
#from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

embeddings = OllamaEmbeddings(model="nomic-embed-text")
db_location = "./chroma_lagchain_db"
add_documents = not os.path.exists(db_location)


if add_documents:
    file_path = "travel_agency_test_brochure.pdf"
    loader = UnstructuredPDFLoader(
    "travel_agency_test_brochure.pdf",
    strategy="hi_res")
    documents = loader.load()
    #loader = PyPDFLoader(file_path)
    # documents = loader.load()

    # # -----------------------
    # # TABLE NORMALIZATION STEP 
    # # -----------------------

    # processed_docs = []

    # for doc in documents:
    #     text = doc.page_content

    #     if "Day" in text and "City" in text and "Activities" in text:
    #         text = text.replace("\n", " ")

    #     processed_docs.append(
    #         doc.copy(update={"page_content": text})
    #     )

    # documents = processed_docs

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

vector_store = Chroma(
    collection_name="tour_details",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=texts)

print(vector_store._collection.count())

peek = vector_store._collection.peek(3)
#print(peek)

search_kwargs={"k": 5}

retriever = vector_store.as_retriever(
    kwargs={"search_kwargs":search_kwargs}
)

# score_threshold- avoid grabage retrieval

# retriever = vector_store.as_retriever(
#     kwargs={"k":5} 
#     # looks up 5 relevant docs
# )

