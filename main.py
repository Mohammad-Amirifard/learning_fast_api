from fastapi import FastAPI

app = FastAPI() # Create a FastAPI instance

# Define a root endpoint.
# We use the @app.get decorator to tell FastAPI that this function
# should handle Http requests to the "/" path.


# Senario 1: User wants to access the root endpoint and get a welcome message.
@app.get("/")
def read_root():
    return {"message": "Hi. Welcome to the first lesson for FastAPI"
    "You are watching the first senario. You are now at root endpoint." }