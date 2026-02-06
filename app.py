# app.py

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from graph import agentic_graph
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
app = FastAPI()

def get_user(token: str = Depends(oauth2)):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        raise HTTPException(status_code=401)

@app.post("/login")
def login():
    token = jwt.encode(
        {"user": "mark", "role": "admin"},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {"access_token": token}

@app.post("/ask")
def ask(question: str, user=Depends(get_user)):
    state = {"question": question, "user": user}
    result = agentic_graph.invoke(state)
    return {
    "status": "success",
    "answer": str(result["answer"])}

