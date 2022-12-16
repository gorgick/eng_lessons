from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 6000
    database_url: str = "sqlite:///./eng_base.sqlite"
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
