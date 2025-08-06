# === main.py ===
from src.config import HF_TOKEN, DATA_PATH, DB_FAISS_PATH, CUSTOM_PROMPT_TEMPLATE
from src.utils import stylish_heading
from src.model_loader import load_llm
from src.prompts import set_custom_prompt
from src.loader import load_pdf_files
from src.chunker import create_chunks
from src.embedding import get_embedding_model
from src.vectorstore import build_vector_db, load_vector_db
from src.qa_chain import setup_qa_chain
import os

#if __name__ == "__main__":
def main():
    stylish_heading()
    print("\n📄 Loading documents and building knowledge base...")

    documents = load_pdf_files(DATA_PATH)
    text_chunks = create_chunks(documents)
    embedding_model = get_embedding_model()

    if not os.path.exists(DB_FAISS_PATH):
        print("🔧 Creating FAISS database...")
        build_vector_db(text_chunks, embedding_model, DB_FAISS_PATH)

    print("✅ Vector DB ready. Launching QA Chat...\n")

    db = load_vector_db(DB_FAISS_PATH, embedding_model)
    llm = load_llm()
    qa_chain = setup_qa_chain(llm, db, set_custom_prompt(CUSTOM_PROMPT_TEMPLATE))

    print("\n🟢 You can start chatting now. Type 'Exit the Chatbot' to end the session.\n")

    while True:
        user_query = input("🧠 You: ")
        if user_query.strip().lower() == "exit the chatbot":
            print("\n👋 Exiting... Have a great day!\n")
            break

        try:
            result = qa_chain.invoke({"query": user_query})
            print(f"🤖 Bot: {result['result']}\n")
        except Exception as e:
            print("❌ Error:", e)