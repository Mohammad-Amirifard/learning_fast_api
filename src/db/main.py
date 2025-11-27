# we try to connect our system to db using the engine.
from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.db.config import Read_Config_from_env as Config

# create an async engine. The engine connects our system to the db.
# We use async engine to allow for asynchronous operations with the database.

engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,# This is the database URL from our config, that tells where our db is located.
    echo=True
))


async def initdb():
    """create a connection to our db"""
    
    async with engine.begin() as conn:
        statement = text("select 'Hello World'")

        result = await conn.execute(statement)

        print(result.all())