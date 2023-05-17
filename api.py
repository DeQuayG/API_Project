from fastapi import FastAPI

app = FastAPI() # Creates an instance of FastAPI

@app.get("/")
async def root():
    return {"message": "Hello World", 
            "message2":"test"}

@app.get("/posts")
def retrieve_posts():
        return ["data_key", "data_value"]