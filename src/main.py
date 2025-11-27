from src.Users.routes import user_router
from src.Movies.routes import movie_router
from src.Books.routes import book_router
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import initdb
"""
Why we we have to use the following code:
The Scenario: The "Heavy Dictionary"
Imagine you are building an app that detects if a user's sentence is Happy or Sad .

To do this, your app needs to load a massive "Brain" (a 3GB AI model file).
The Bad Way: You load the 3GB brain every single time a user sends a text. The user waits 10 seconds for a "Hello".
The Good Way (Lifespan): You load the 3GB brain once when the server turns on. The user gets an instant reply.
"""
@asynccontextmanager
async def life_span(app:FastAPI):
    print('Server is starting...')
    await initdb() # Be careful with await here. If initdb is not async, do not use await.
    yield
    print('Server has been stoped')
app = FastAPI(

    title="My Multi-Module API",
    description="An API that manages users, movies, and books.",
    version="1.0.0",
    lifespan = life_span
)
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(movie_router, prefix="/movies", tags=["movies"])
app.include_router(book_router, prefix="/books", tags=["books"])