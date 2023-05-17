from fastapi import FastAPI

app = FastAPI() # Creates an instance of FastAPI

# This is a "Path Operation" or a "Route"
# This is a regular function, the 'async' part is only necesarry 
# if you're performing fucntions 'asynchronously'

# The function's name of 'root' is arbitrary, you could name it 
# anything, as it's just a regular function, although you should probably name it something 
# that relates to what it's doing. If it's a 'user_login' function, you can
# name it as such

# JSON is the main universal language for API's, which is why the "return" 
# statement automatically converts to JSON with Fast API


@app.get("/")
async def root():
    return {"message": "Hello World", 
            "message2":"test"}
# This code snippet is straight from the FastAPI Documentation

# The line "@app.get("/")" is a python decorator. Without the 
# decorator the function woun't be associated with Fast API. It would 
# just be a regular function. 
# The "@" is what clarifies that it will be a decorator, then you reference
# The fast API Instance

@app.get("/posts")
def retrieve_posts():
        return ["data_key", "data_value"]