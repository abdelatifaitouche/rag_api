from fastapi import FastAPI
from chatbot import chatbot


#GET : Send data and returing a reponse 

#POST : create something in the database

#PUT  : Update something in the database

#DELETE : Delete somehting in the DB

app = FastAPI()







@app.get('/')
def chatbot_app(query : str):
    response = chatbot(query)
    return {'data' : response}