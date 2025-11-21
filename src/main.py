from src.Users.routes import user_router
from src.Movies.routes import movie_router
from src.Books.routes import book_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(movie_router, prefix="/movies", tags=["movies"])
app.include_router(book_router, prefix="/books", tags=["books"])