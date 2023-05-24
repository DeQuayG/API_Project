from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional

app = FastAPI() # Creates an instance of FastAPI

@app.get("/")
def landing_page():
    return {"message": "Hello World", 
            "message2":"test"}

@app.get("/posts")
def retrieve_posts():
        return ["data_key", "data_value"]

@app.post("/send")
def send_data(data: dict = Body(...)):
      return ["Data Successfuly sent", "The body of the data sent is here ", data] 
      #^^ This by itself is bascially just an HTTP 200 reponse 