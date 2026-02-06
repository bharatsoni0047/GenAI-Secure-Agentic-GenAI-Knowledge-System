import os
from dotenv import load_dotenv

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")


# tools.py
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import ollama
from sqlalchemy import create_engine, text

# Load models
embedding_model = SentenceTransformer("BAAI/bge-base-en-v1.5")

# Chroma DB
client = chromadb.Client(
    Settings(
        persist_directory="chroma_db",
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection("agenticrag")

# Embedding
def embed_text(text):
    return embedding_model.encode(text).tolist()

# Vector DB add
def add_to_vector_db(texts, metadatas, ids):
    embeddings = [embed_text(t) for t in texts]
    collection.add(
        documents=texts,
        metadatas=metadatas,
        ids=ids,
        embeddings=embeddings
    )

# Vector DB search
def search_vector_db(query):
    return collection.query(
        query_embeddings=[embed_text(query)],
        n_results=3
    )

# LLM call
LLM_MODEL_NAME = "phi3"
def llm_generate(prompt):
    res = ollama.chat(
        model=LLM_MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return res["message"]["content"]

# Text to SQL
def text_to_sql(question, table_name):
    prompt = f"""
    Convert the question to a valid MySQL SQL query.
    Return ONLY raw SQL. No markdown. No explanation.
    Table: {table_name}
    Question: {question}
    """

    sql = llm_generate(prompt)

    # clean markdown if LLM still adds it
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql


# Run SQL
def run_sql(db_url, sql):
    engine = create_engine(db_url)
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        return [list(row) for row in rows]

