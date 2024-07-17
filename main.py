from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello world?"}

@app.get("/quote")
def generate_quote():
    return{"quote": "This is ewdwedw"}