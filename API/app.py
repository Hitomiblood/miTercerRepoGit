import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows


@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg", "Robin"]
    return rows


@app.get("/CursosPlatzi")
def get_cursos():
    rows = ["Python", "Django", "Flask", "FastAPI", "JavaScript", "React", "Vue", "Angular", "NodeJS", "MongoDB"]
    return rows


