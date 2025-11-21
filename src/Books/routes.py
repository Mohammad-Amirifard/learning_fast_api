# This file is called routes.py sicnee it contains all the routes related to users
from fastapi import APIRouter
from src.Books.book_data import users_fav_books
book_router = APIRouter()

"""
Senario 1: User wants to access the root endpoint and get a welcome message.
Goal: Learning the endpoint creation in FastAPI.

"""
@book_router.get("/")
def read_root():
    return {"message": "Hi. Welcome to the first lesson for FastAPI"
    "You are watching the first senario. You are now at root endpoint related to book route." }


# Let's allow user to get all books.
@book_router.get("/books_root/books_list")
def read_all_moives()->dict:
    return users_fav_books

"""


Senario 4: User wants to access an endpoint that uses both path and query parameters.
Suppose we have lots of favorite books stored per each user, now uers wnat to see just a sepcific book from his favorite list.
"""


@book_router.get("/favorite_books/{user_id}")
def read_some_of_fav_books(user_id:int=1,maximum_number:int=5)->dict:
    if not user_id in users_fav_books.keys():
        return {"msg":"Sorry, your user id is not in our list"}
    
    user_books = list(users_fav_books[user_id].values())[:maximum_number]
    return {"Your favorite books are: ":user_books}
    

