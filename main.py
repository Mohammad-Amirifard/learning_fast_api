from fastapi import FastAPI

app = FastAPI() # Create a FastAPI instance

# Define a root endpoint.
# We use the @app.get decorator to tell FastAPI that this function
# should handle Http requests to the "/" path.

"""
Senario 1: User wants to access the root endpoint and get a welcome message.
Goal: Learning the endpoint creation in FastAPI.

"""

@app.get("/")
def read_root():
    return {"message": "Hi. Welcome to the first lesson for FastAPI"
    "You are watching the first senario. You are now at root endpoint." }


"""
Senario 2: User wants to access his specified endpoint and see some registered detail from past.
Goal: Learning the path parameters.

"""
# Create a dictionary to simulate a database of users.
user_db ={
    1:{"name": "Alice", "age": 30,'email':"alice@gamil.com"},
    2:{"name": "Bob", "age": 25, 'email':"bob@gamil.com"},
    3:{"name": "Charlie", "age": 35, 'email':"charlie@gamil.com"}
}

# use decorator to define a path parameter.
@app.get("/users/{user_id}")
def read_user(user_id:int)-> dict:
    user_detail =user_db.get(user_id)
   
    if not user_detail:
        return {'msg':"your id is not in our system. Please use the correct one"}
    
    name = user_detail['name']
    age = user_detail['age']
    email = user_detail['email']
    return {"msg":(f'Hi {name}. Welcome to this path'
                        f'You are in the scenario 2 to learn path parameter.'
                        f'you can see you detail in the following:'
                        f'Email: {email} and Age:{age}'
                        )
                }
    
    
