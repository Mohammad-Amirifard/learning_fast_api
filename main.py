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
    
    
"""
Senario 3: User wants to access an endpoint with query parameters to filter data.
Here, suppopse we have an endpoint shows all films, but using query parameters, user can filter films by genre and year.
Goal: Learning the query parameters.
"""


movies_db = {
    1: {"title": "Inception", "genre": "Sci-Fi", "year": 2010},
    2: {"title": "The Dark Knight", "genre": "Action", "year": 2008},
    3: {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014},
    4: {"title": "Pulp Fiction", "genre": "Crime", "year": 1994},

}

# Let's allow user to get all movies.
@app.get("/movies/")
def read_all_moives()->dict:
    return movies_db

#Let's see movies just by an specific genre
@app.get('/movies/filter1')
def read_moives_by_genre(genre: str="Sci-Fi"):
    movies_by_genre = {}
    for id, dic in movies_db.items():
        if dic.get("genre") == genre:
            movies_by_genre[id] = dic
    
    if movies_by_genre:
        return movies_by_genre
    return {"msg":"No matched movies found"}

#Let's see movies just by an specific genre and specified year
@app.get('/movies/filter2')
def read_movies_by_genre_year(genre:str="Sci-Fi", year: int=2010):
    movies_dic = {}
    for id, dic in movies_db.items():
        if dic['genre']==genre and dic["year"]==year:
            movies_dic[id] = dic
    
    if movies_dic:
        return movies_dic
    return {"msg":"No matched movies found"}

"""
Senario 4: User wants to access an endpoint that uses both path and query parameters.
Suppose we have lots of favorite books stored per each user, now uers wnat to see just a sepcific book from his favorite list.
"""
users_fav_books = {
    1: {1: "1984", 2: "To Kill a Mockingbird", 3: "The Great Gatsby",4:"Gulliver's Travels",5:"Madame Bovary"},
    2: {1: "Moby", 2: "War and Peace", 3: "Hamlet",4:"The Odyssey",5:"Ulysses"},
    3: {1: "The Catcher in the Rye", 2: "Brave New World", 3: "The Hobbit",4:"Fahrenheit 451",5:"Jane Eyre"},
}

@app.get("/favorite_books/{user_id}")
def read_some_of_fav_books(user_id:int=1,maximum_number:int=5)->dict:
    if not user_id in users_fav_books.keys():
        return {"msg":"Sorry, your user id is not in our list"}
    
    user_books = list(users_fav_books[user_id].values())[:maximum_number]
    return {"Your favorite books are: ":user_books}
    

"""
Senario 5: Suppose in scenario 4, user forgets to write the maximum number and we don't want to show defulat value to him/her.
Gaol: Learn Optional module.
"""
from typing import Optional
@app.get("/new_favorite_books/{user_id}")
def read_some_of_fav_books(user_id:int,maximum_number:Optional[int]=None)->dict:
    if maximum_number is None:
        return {"msg": "You didn't enter any maximum_number. We got None for it."}
    if user_id not in users_fav_books.keys():
        return {"msg": "Sorry, your user id is not in our list."}
        
    user_books = list(users_fav_books[user_id].values())[:maximum_number]
    return {"Your favorite books are: ": user_books}