from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def helloWord():
    return {
        "msg": "hello world"
    }


class Persona(BaseModel):
    name: str
    sex: str
    id: Optional[str]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = str(id(self))


BD = [Persona(
    name='Daniel Alejandro', sex="M"), Persona(
    name='Laura de la portilla', sex="F"), Persona(name='Ramona la fea', sex='B')]


@app.get('/nombres')
def get_names():
    return BD


@app.post("/nombres")
def create_new_name(new_persona: Persona):
    BD.append(
        new_persona
    )
    return new_persona


@app.delete('/nombres/{_id}')
def get_names(_id):
    index = -1
    for i, persona in enumerate(BD):
        if persona.id == _id:
            index = i
            break
    if index > -1:
        BD.pop(index)
    return {
        "remove": _id
    }
