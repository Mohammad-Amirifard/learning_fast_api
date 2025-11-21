#This file contains all validation schemes related to moviesfrom pydantic import BaseModel
from pydantic import BaseModel
# First we need to tell what sheme the data sent by user must have
class Movie_structure(BaseModel):
    title : str # It says the title given by user must be str
    genre : str
    year : int

