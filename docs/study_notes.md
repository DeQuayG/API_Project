from fastapi import FastAPI

app = FastAPI() # Creates an instance of FastAPI

 This is a "Path Operation" or a "Route"
 This is a regular function, the 'async' part is only necesarry 
 if you're performing fucntions 'asynchronously'

 The function's name of 'root' is arbitrary, you could name it 
 anything, as it's just a regular function, although you should probably name it something 
 that relates to what it's doing. If it's a 'user_login' function, you can
 name it as such

 JSON is the main universal language for API's, which is why the "return" 
 statement automatically converts to JSON with Fast API


@app.get("/")
async def root():
    return {"message": "Hello World", 
            "message2":"test"}
# This code snippet is straight from the FastAPI Documentation

# The line "@app.get("/")" is a python decorator. Without the 
# decorator the function woun't be associated with Fast API. It would 
# just be a regular function. 
# The "@" is what clarifies that it will be a decorator, then you reference the fast API Instance

@app.get("/posts")
def retrieve_posts():
        return ["data_key", "data_value"]


The "get" is the HTTP Method we're using within thsi path operation. So like with all CRUD operations, you could also use "put", "post", "delete", etc.


Whenever you launch the API, FastAPI will go down the list of your path operations and use the first matching condition, so if you have two paths that say "/users", FastAPI will use the first one (from top to bottom) and ignore the others

With "post" requests, we are sending data instead of retrieving data from the API. Within Postman you can send data to the API by using the "Body" header and using JSON. JSON format is basically Python dictionaries, it uses curly braces and key-value pairing for the data. 

!!! Example 
""" "data" : "Sample data placed here", 
    "type" : "Raw JSON"

"""



@app.post("/send")
def send_data(data: dict = Body(...)):
      return ["Data Successfuly sent", "The body of the data sent is here ", data] 

^^ This code snippet will return the data sent by a POST request. In Postman we sent the data in JSON format, and this path oiperation will return that data in the form of a dictionary. 
    - 'data': data is just a variable name, it could be 'payload', 'packet', etc
    - 'dict': The typing of the 'data'
    - 'Body': A built-in of FastAPI. 

The function will take the all of the fields from the 'Body' of the request, convert that data into a Python dictionary, and then store it within a variable named 'data'.