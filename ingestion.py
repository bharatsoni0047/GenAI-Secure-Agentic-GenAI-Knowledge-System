# ingestion.py
import fitz
import pandas as pd
import pytesseract
from PIL import Image
import uuid
from tools import add_to_vector_db

def ingest_pdf(path):
    doc = fitz.open(path)
    texts = [p.get_text() for p in doc if p.get_text().strip()]
    add_to_vector_db(
        texts,
        [{"source": path}] * len(texts),
        [str(uuid.uuid4()) for _ in texts]
    )

def ingest_excel(path):
    df = pd.read_excel(path)
    text = df.to_string()
    add_to_vector_db(
        [text],
        [{"source": path}],
        [str(uuid.uuid4())]
    )

def ingest_image(path):
    text = pytesseract.image_to_string(Image.open(path))
    if text.strip():
        add_to_vector_db(
            [text],
            [{"source": path}],
            [str(uuid.uuid4())]
        )
