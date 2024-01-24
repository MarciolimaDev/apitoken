from fastapi import FastAPI

app = FastAPI()

@app.get("/tokenbm")
def read_root():
    return {"id": "1", "name": "tokenbm", "token": "UNzQ4mDY-l7lFPjHdntg"}
