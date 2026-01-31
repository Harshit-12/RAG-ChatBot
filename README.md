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
  
