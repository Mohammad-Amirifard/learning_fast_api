# inside src/config.py
# This file tries look at the .env file and extract its connection url
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str 

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"
    )

# add this line    
Read_Config_from_env = Settings()

#You can test it by following code
#print(Read_Config_from_env.DATABASE_URL)