# 🎥 YouTube Video Chatbot

An AI-powered YouTube Video Chatbot that allows users to chat with YouTube videos using transcript-based Retrieval-Augmented Generation (RAG).

Users can simply paste a YouTube video URL, and the application automatically extracts the transcript, creates embeddings, stores them in a FAISS vector database, and answers questions using Google's Gemini LLM.

---
## 🌐 Live Demo

🚀 Try the application here:

👉 https://youtube-ai-assistant-1926.streamlit.app/
---

## 🚀 Features

- 🎥 Accepts YouTube Video URLs
- 📝 Automatically extracts video transcripts
- ✂️ Splits transcript into chunks using LangChain
- 🧠 Generates embeddings with Gemini Embedding Model
- 🗂️ Stores embeddings in FAISS Vector Database
- 🔍 Retrieves relevant transcript chunks using Similarity Search
- 🤖 Answers user questions using Gemini 2.5 Flash
- 💬 Interactive chat interface with Streamlit
- ⚡ Fast Retrieval-Augmented Generation (RAG)

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
YouTube URL
  │
  ▼
Transcript Extraction
(YouTube Transcript API)
  │
  ▼
Text Splitting
(LangChain Text Splitter)
  │
  ▼
Embeddings Creation
(Gemini Embedding Model)
  │
  ▼
FAISS Vector Database
  │
  ▼
User Question
  │
  ▼
Similarity Search
  │
  ▼
Relevant Context
  │
  ▼
Gemini 2.5 Flash
  │
  ▼
Final Answer
```

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Programming Language | Python |
| LLM | Gemini 2.5 Flash |
| Embeddings | Gemini Embedding 001 |
| Framework | LangChain |
| Vector Database | FAISS |
| Transcript Extraction | YouTube Transcript API |

---

## 📂 Project Structure

```text
youtube-video-chatbot/
│
├── app.py
├── requirements.txt
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-video-chatbot.git
cd youtube-video-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Gemini API Key

Create a folder named:

```text
.streamlit
```

Inside it create:

```text
secrets.toml
```

Add your Gemini API Key:

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will run at:

```text
http://localhost:8501
```

---

## 📋 How It Works

### Step 1
Paste a YouTube video URL.

### Step 2
The transcript is extracted automatically.

### Step 3
Transcript is split into smaller chunks.

### Step 4
Embeddings are generated using Gemini.

### Step 5
Embeddings are stored in a FAISS vector database.

### Step 6
Ask questions related to the video.

### Step 7
Relevant chunks are retrieved using similarity search.

### Step 8
Gemini generates an answer using the retrieved context.

---

## 💡 Example Questions

```text
Summarize this video.

What are the main topics discussed?

Explain the key concepts mentioned.

What tools are used in this tutorial?

Give me the important points from this video.
```

---

## 📸 Sample Workflow

```text
YouTube URL
      ↓
Transcript Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
Question
      ↓
Similarity Search
      ↓
Gemini Response
```

---

## 🔮 Future Improvements

- Multiple Video Support
- Chat History
- Conversation Memory
- Source References
- Download Chat as PDF
- Multi-Language Support
- Hybrid Search (Keyword + Semantic)
- YouTube Playlist Chatbot

---

## 👨‍💻 Author

Harsha

Aspiring AIML Engineer | Python Developer | GenAI Enthusiast

---

## ⭐ If you found this project useful

Give this repository a star ⭐ and support the project.
add projectlink:https://youtube-ai-assistant-1926.streamlit.app/
