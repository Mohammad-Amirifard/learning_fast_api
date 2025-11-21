# This file is called routes.py sicnee it contains all the routes related to movies
from fastapi import APIRouter
from src.Movies.moives_data import movies_db
from src.Movies.schemes import Movie_structure
movie_router = APIRouter()



"""
Senario 1: User wants to access the root endpoint and get a welcome message.
Goal: Learning the endpoint creation in FastAPI.

"""

@movie_router.get("/")
def read_root():
    return {"message": "Hi. Welcome to the first lesson for FastAPI"
    "You are watching the first senario. You are now at root endpoint related to movie route." }


"""
Senario 3: User wants to access an endpoint with query parameters to filter data.
Here, suppopse we have an endpoint shows all films, but using query parameters, user can filter films by genre and year.
Goal: Learning the query parameters.
"""


# Let's allow user to get all movies.
@movie_router.get("/movies_list")
def read_all_moives()->dict:
    return movies_db

#Let's see movies just by an specific genre
@movie_router.get('/by_genre/')
def read_moives_by_genre(genre: str="Sci-Fi"):
    movies_by_genre = {}
    for id, dic in movies_db.items():
        if dic.get("genre") == genre:
            movies_by_genre[id] = dic
    
    if movies_by_genre:
        return movies_by_genre
    return {"msg":"No matched movies found"}



#Let's see movies just by an specific genre and specified year
@movie_router.get('/by_genre_year/')
def read_movies_by_genre_year(genre:str="Sci-Fi", year: int=2010):
    movies_dic = {}
    for id, dic in movies_db.items():
        if dic['genre']==genre and dic["year"]==year:
            movies_dic[id] = dic
    
    if movies_dic:
        return movies_dic
    return {"msg":"No matched movies found"}


"""
Scenario 6: User watns to send data to the server using POST method.
Here, we need first to check the structure of the data sended by user by pydantic model.
Suppose user wants to add a new movie to his/her list.
"""


@movie_router.post("/add_fav_books")
def add_fav_books(movie_detail:Movie_structure): # Here the input of user is called movie_detail which must pay attention to calss Movie_Structure for checing inout format
    
    # Now we can add this movie to the movies_db
    # Compute the next numeric id in a safe way (handle empty DB)
    if movies_db:
        new_id = max(movies_db.keys()) + 1
    else:
        new_id = 1

    # Store the Pydantic model as a plain dict so responses are JSON-serializable
    movies_db[new_id] = movie_detail.dict()
    return {'State': "Successful", 'Movies': movies_db}


"""
Scenario 7: User watns to see all movies, but these data sending from server to user must be validated by pydantic.
Here, we need first to check the structure of the data sended by server not user by pydantic model.
"""

# We created before Movie_structure before
from typing import List
@movie_router.get("/movies_list_validated", response_model=List[Movie_structure])
def read_all_moives_validated():
    return list(movies_db.values())


"""
Scenario 8: User watns to send data to the server using POST method.
Here, we want to understand http statis.
Suppose user wants to add a new movie to his/her list.
"""

from fastapi import status
@movie_router.post("/add_fav_books_handle_status", status_code=status.HTTP_201_CREATED)
def add_fav_books(movie_detail:Movie_structure): # Here the input of user is called movie_detail which must pay attention to calss Movie_Structure for checing inout format
    
    # Now we can add this movie to the movies_db
    # Compute the next numeric id in a safe way (handle empty DB)
    if movies_db:
        new_id = max(movies_db.keys()) + 1
    else:
        new_id = 1

    # Store the Pydantic model as a plain dict so responses are JSON-serializable
    movies_db[new_id] = movie_detail.dict()
    return {'State': "Successful", 'Movies': movies_db}


"""
Scenario 9: Update an existing movie using PUT method.
"""
@movie_router.put("/update_movie/{movie_id}")
def update_movie(movie_id:int, movie_detail:Movie_structure):
    if movie_id not in movies_db:
        return {"msg":"Movie id not found."}
    
    movies_db[movie_id] = movie_detail.dict()
    return {'State':"Successful", 'Updated Movie': movies_db[movie_id]}

"""
Scenario 10: Delete an existing movie using DELETE method.
"""
@movie_router.delete("/delete_movie/{movie_id}")
def delete_movie(movie_id:int):
    if movie_id not in movies_db:
        return {"msg":"Movie id not found."}
    
    deleted_movie = movies_db.pop(movie_id)
    return {'State':"Successful", 'Deleted Movie': deleted_movie}