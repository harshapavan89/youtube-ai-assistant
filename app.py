import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_community.vectorstores import FAISS
def get_video_id(url):

    # Short URL
    if "youtu.be" in url:
        return url.split("/")[-1].split("?")[0]

    parsed_url = urlparse(url)

    # Normal YouTube URL
    if parsed_url.hostname in [
        "www.youtube.com",
        "youtube.com",
        "m.youtube.com"
    ]:
        return parse_qs(
            parsed_url.query
        ).get("v", [None])[0]

    # Embed URL
    if parsed_url.path.startswith("/embed/"):
        return parsed_url.path.split("/")[2]

    return None
# ==================================
# PAGE TITLE
# ==================================

st.set_page_config(page_title="YouTube Video Chatbot")
st.title("🎥 YouTube Video Chatbot")

# ==================================
# SESSION STATE
# ==================================

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "video_processed" not in st.session_state:
    st.session_state.video_processed = False

# ==================================
# URL INPUT
# ==================================

youtube_url = st.text_input(
    "Enter YouTube Video URL:"
)

# Video Preview
if youtube_url:
    st.video(youtube_url)

# ==================================
# PROCESS VIDEO
# ==================================

if st.button("Process Video"):

    if not youtube_url:
        st.warning("Please enter a YouTube URL")
        st.stop()

    try:

        # Extract Video ID
        video_id = get_video_id(youtube_url)

        if not video_id:
            st.error("Invalid YouTube URL")
            st.stop()

        # ==========================
        # TRANSCRIPT EXTRACTION
        # ==========================

        with st.spinner("🎥 Loading Transcript..."):
        
            api = YouTubeTranscriptApi()

            transcript = api.fetch(video_id)

            text = " ".join(
                snippet.text
                for snippet in transcript
            )

        st.success("✅ Transcript Loaded")

        # ==========================
        # TEXT SPLITTING
        # ==========================

        with st.spinner("✂️ Creating Chunks..."):

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_text(text)

        st.success("✅ Chunks Created")

        # ==========================
        # EMBEDDINGS
        # ==========================

        with st.spinner("🧠 Creating Embeddings..."):

            embeddings = GoogleGenerativeAIEmbeddings(
                model="models/gemini-embedding-001",
                google_api_key=st.secrets["GEMINI_API_KEY"]
            )

            vector_store = FAISS.from_texts(
                texts=chunks,
                embedding=embeddings
            )

        # Save in Session State

        st.session_state.vector_store = vector_store
        st.session_state.video_processed = True

        st.success("✅ Vector Database Created")
        st.success("🚀 Video Ready For Chat")

    except Exception as e:
        st.error(str(e))

# ==================================
# CHAT SECTION
# ==================================

if st.session_state.video_processed:

    question = st.chat_input(
        "Ask anything about this video..."
    )

    if question:

        try:

            # User Message
            st.chat_message("user").write(question)

            # Get Vector Store
            vector_store = st.session_state.vector_store

            # ======================
            # RETRIEVAL
            # ======================

            docs = vector_store.similarity_search(
                question,
                k=4
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            # ======================
            # GEMINI LLM
            # ======================

            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=st.secrets["GEMINI_API_KEY"]
            )

            # ======================
            # PROMPT
            # ======================

            prompt = f"""
            You are a helpful YouTube Video Assistant.

            Answer only from the provided context.

            If the answer is not available in the context,
            reply:

            The answer is not available in the video transcript.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """

            # ======================
            # GENERATE ANSWER
            # ======================

            with st.spinner("🤔 Thinking..."):

                response = llm.invoke(prompt)

            # Assistant Message
            st.chat_message("assistant").write(
                response.content
            )

        except Exception as e:
            st.error(str(e))