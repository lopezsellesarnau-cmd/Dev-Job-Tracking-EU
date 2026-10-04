from fastapi import FastAPI
from db import get_counts

app = FastAPI()


@app.get("/counts")
def counts():
    return get_counts()
