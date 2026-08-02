from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "OmniAssist AI"
    VERSION: str = "1.0.0"

    OPENAI_API_KEY: str = ""
    GROQ_API_KEY: str = ""

    CHROMA_DB_PATH: str = "./data/vector_db"

    class Config:
        env_file = ".env"


settings = Settings()