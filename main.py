from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("q-fastapi.csv")


@app.get("/api")
def get_students(class_: List[str] = Query(None, alias="class")):
    if class_:
        filtered = df[df["class"].isin(class_)]
    else:
        filtered = df
    result = filtered.to_dict(orient="records")
    return {"students": result}
