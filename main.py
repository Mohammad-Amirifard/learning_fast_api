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