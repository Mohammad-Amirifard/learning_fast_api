# This file is called routes.py sicnee it contains all the routes related to users
from fastapi import APIRouter
from src.Users.users_data import user_database



"""
Senario 1: User wants to access the root endpoint and get a welcome message.
Goal: Learning the endpoint creation in FastAPI.

"""
user_router = APIRouter()
@user_router.get("/")
def read_root():
    return {"message": "Hi. Welcome to the first lesson for FastAPI"
    "You are watching the first senario. You are now at root endpoint related to user route." }




"""
Senario 2: User wants to access his specified endpoint and see some registered detail from past.
Goal: Learning the path parameters.

"""
# use decorator to define a path parameter.
user_db = user_database()
@user_router.get("/{user_id}")
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
    