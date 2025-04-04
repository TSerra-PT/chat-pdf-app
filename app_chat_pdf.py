import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from tempfile import NamedTemporaryFile

# Configuração da API Key
openai_api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")
st.title("📄💬 Chat com PDF")

uploaded_file = st.file_uploader("Carrega um ficheiro PDF", type=["pdf"])

if uploaded_file and openai_api_key:
    with st.spinner("📚 A ler o documento..."):
        # Guardar temporariamente o ficheiro
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        # Processar o PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load_and_split()
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        db = FAISS.from_documents(documents, embeddings)
        retriever = db.as_retriever()
        chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key),
            retriever=retriever
        )
        st.success("✅ Pronto para conversar!")

        # Caixa de chat
        question = st.text_input("✍️ Escreve a tua pergunta:")
        if question:
            with st.spinner("A pensar..."):
                answer = chain.run(question)
                st.markdown(f"**💬 Resposta:** {answer}")
else:
    st.info("🔑 Introduz a tua OpenAI API Key e carrega um PDF.")