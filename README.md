# Local PDF RAG Service

A fully offline, CPU-only Retrieval-Augmented Generation (RAG) system for question answering based on PDF documents. It uses **LangChain**, **Ollama** for local LLMs and embeddings, combined with **ChromaDB** for vector storage, ensuring hallucination-free responses grounded strictly in the provided PDF content.

## Features
✅ **Fully Offline / Local**: Runs entirely on your machine without internet access.  
✅ **CPU-Only**: No GPU required; works on systems with ~6GB RAM.  
✅ **PDF-Based Question Answering**: Upload a PDF and query its contents intelligently.  
✅ **Hallucination-Safe**: Strict grounding ensures answers are derived only from the PDF—no fabrications.  
✅ **Clean Separation of Concerns**: Modular design with clear components for embedding, storage, and querying.

## Prerequisites
- **System Requirements**:
  - Windows, Linux, or macOS.
  - Python 3.9 or higher.
  - ~6GB RAM (no GPU needed).

## Installation

### 1. Install Ollama
Download and install Ollama from the official website:  
👉 [https://ollama.com/download](https://ollama.com/download)

Verify the installation:  
```ollama --version```


### 2. Pull Required Ollama Models
First, pull the required embedding model:  
```ollama pull nomic-embed-text```

Choose and pull one LLM model:  
- Lightweight option (compatible with the code):
  ollama pull phi
- Recommended for better Hinglish support:
```ollama pull qwen2.5:3b```


Verify the models are available:    
```ollama list```


### 3. Set Up Python Environment (RAG Service)
Create and activate a virtual environment:  
```python -m venv venv```
- On Linux/macOS:
  ```source venv/bin/activate```
- On Windows:
```venv\Scripts\activate```


Install dependencies (assuming a `requirements.txt` file is provided; if not, install `chromadb`, `langchain`, and any other needed packages manually):  
```pip install -r requirements.txt```

### 4. Set Up Vector Store
The `vector.py` script handles PDF processing:  
- Loads the PDF.  
- Splits it into manageable chunks.  
- Generates embeddings using the pulled model.  
- Stores embeddings in ChromaDB.  

📌 **Important**: The database is created only once. If you need to re-index (e.g., for a new PDF), delete the `chroma_langchain_db/` directory and re-run the script.

## Usage
1. Ensure Ollama is running in the background:
   ```ollama serve```
2. Run the main.py
   ```python .\main.py```

(Adjust based on your implementation; responses will be grounded in the PDF content.)

## Known Limitations
🧪 **Strictly PDF-Bound**: Answers are limited to information explicitly in the PDF—no external knowledge.  
🧪 **No Image Understanding**: Text-only extraction; images, tables, or visuals in the PDF are not processed.  
🧪 **No Internet Access**: Fully local, so no real-time updates or web searches.  
🧪 **No Fine-Tuning**: Designed for out-of-the-box use without model customization.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests for improvements, bug fixes, or new features.

📘 README.md — RAG Travel Assistant with LangChain, Ollama & Chroma
🌍 RAG Travel Assistant — PDF-Based Tour & Travel Chatbot

This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to ask natural-language questions about travel agency brochures and tour packages stored in PDFs.

## It supports:

Multi-page brochures

Day-wise itineraries

Routes & destinations

Pricing tables

Hotel listings

Inclusions / exclusions

Policies & FAQs

The system uses:

LangChain for orchestration

Ollama for local LLM inference

ChromaDB for vector storage

UnstructuredPDFLoader for PDF parsing

Streamlit for the web UI

## 🧠 Architecture Overview
PDF Documents
     ↓
UnstructuredPDFLoader
     ↓
Table Normalization & Cleaning
     ↓
Chunking (400 tokens, overlap 50)
     ↓
Embeddings via Ollama
     ↓
Chroma Vector Database
     ↓
Retriever (Top-K semantic search)
     ↓
LLM + Strict Prompt
     ↓
Web UI (Streamlit)

## ✨ Key Features
## ✅ PDF Intelligence

Supports complex multi-page brochures

Extracts tables such as itineraries and pricing

OCR-ready using Tesseract (optional)

Normalizes tables into readable text before embedding

## ✅ Table-Aware RAG

Special preprocessing converts table rows into LLM-friendly text so the model can correctly answer:

"What is the day-wise itinerary?"
"Which city is visited on Day 3?"
"What is the total cost for the Dubai tour?"

## ✅ Hallucination Control

To prevent creative drift:

Temperature set to 0.0

Output token limit (num_predict)

Strict RAG prompt instructions

Limited retrieval size (k=6–8)

Forced refusal when data is missing

## ✅ Web Interface

Browser-based UI using Streamlit

Ask & Reset buttons

Loading spinner

Cancel generation mid-response

Retrieved-context viewer for debugging
  
## Below are some of the test results


<img width="979" height="580" alt="image" src="https://github.com/user-attachments/assets/8f58cd52-ead2-459b-936e-f520925aa46b" />

<img width="979" height="505" alt="image" src="https://github.com/user-attachments/assets/b001792c-a5d1-4c4a-8f62-f7749d40c16c" />

<img width="979" height="539" alt="image" src="https://github.com/user-attachments/assets/5ade9beb-e4aa-4f6b-b6fa-2ce7a657a5ba" />

<img width="890" height="332" alt="image" src="https://github.com/user-attachments/assets/85853f5d-b62b-429e-8886-b603b1941706" />

<img width="1184" height="698" alt="image" src="https://github.com/user-attachments/assets/c6057e59-4cae-40e6-8ae6-70afa8571191" />

<img width="828" height="457" alt="image" src="https://github.com/user-attachments/assets/338c18b7-010d-4cbf-a110-0237b2f9e1e1" />





