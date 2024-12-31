from fastapi import FastAPI



#GET : Send data and returing a reponse 

#POST : create something in the database

#PUT  : Update something in the database

#DELETE : Delete somehting in the DB

app = FastAPI()

inventory = {
    1 : {
        'name':'Milk',
        'price' : 3.99 , 
        "quantity" : 40
    }
}

@app.get('/get-item/{item_id}')
def get_item(item_id : int):
    return inventory[item_id]