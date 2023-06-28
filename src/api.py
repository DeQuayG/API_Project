from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI() # Creates an instance of FastAPI


class Post(BaseModel):
      title: str or int
      content: str 
      public_post: bool = True

@app.get("/")
def landing_page():
    return {"message": "Hello World", 
            "message2":"test"}

@app.get("/posts")
def retrieve_posts():
        return ["data_key", "data_value"]

@app.post("/send_data")
def send_data(new_post: Post): 
      print(new_post.dict)
      return ["Posted Successfully", new_post] 
      #^^ This by itself is bascially just an HTTP 200 reponse 