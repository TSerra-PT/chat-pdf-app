import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from tempfile import NamedTemporaryFile

# Configuration of API Key
openai_api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")
st.title("📄💬 Chat with PDF")

uploaded_file = st.file_uploader("Load a PDF file", type=["pdf"])

if uploaded_file and openai_api_key:
    with st.spinner("📚 Reading the document..."):
        # Save temporarily the file
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        # Processing the PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load_and_split()
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        db = FAISS.from_documents(documents, embeddings)
        retriever = db.as_retriever()
        chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key),
            retriever=retriever
        )
        st.success("✅ Ready to talk!")

        # Caixa de chat
        question = st.text_input("✍️ Write your question:")
        if question:
            with st.spinner("Thinking..."):
                answer = chain.run(question)
                st.markdown(f"**💬 Answer:** {answer}")
else:
    st.info("🔑 Put your OpenAI API Key and load a pdf file.")
