# 📄💬 Chat with PDF (Streamlit + Langchain)

This is a simple Streamlit app that allows you to chat with the contents of a PDF using natural language. It leverages LLMs (like GPT-3.5/4), Langchain, and embeddings to create an intelligent assistant for documents.

---

## 🚀 Features

- 📁 Upload and read PDF files
- 💬 Ask questions in natural language
- 🤖 Powered by OpenAI GPT (3.5 or 4)
- 🔍 Semantic search with embeddings
- 🌐 Easy-to-use web interface via Streamlit

---

## 🧰 Tech Stack

- [Langchain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- FAISS (vector store)
- PyPDF (PDF parsing)

---

## 🛠️ How to Run Locally

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/chat-pdf-app.git
cd chat-pdf-app
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the app**:

```bash
streamlit run app_chat_pdf.py
```

4. Enter your OpenAI API Key and upload a PDF to start chatting!

---

## ☁️ Deploy on Streamlit Cloud

1. Sign up at: https://streamlit.io/cloud
2. Link your GitHub repository
3. Set the main file path to `app_chat_pdf.py`
4. Deploy and get your public app link 🎉

---

## 🔐 Security

Your OpenAI API Key is never stored. It’s entered client-side and only used during the session.

---

## 📌 Example Use

> Question: “What is the delivery deadline mentioned in the contract?”  
> Answer: “The standard delivery term is 30 days after signature.”

---

## 📬 Contributing

Feel free to open issues or submit pull requests. Suggestions and improvements are welcome!

---

## 📜 License

MIT License © [Your Name or GitHub Handle]