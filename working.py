from fastapi import FastAPI
from chatbot import chatbot
from fastapi.middleware.cors import CORSMiddleware



#GET : Send data and returing a reponse 

#POST : create something in the database

#PUT  : Update something in the database

#DELETE : Delete somehting in the DB

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def chatbot_app(query : str):
    response = chatbot(query)
    return response