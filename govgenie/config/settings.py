"""
Central config — all values come from .env so nothing is hardcoded.
Import this anywhere: from govgenie.config.settings import settings
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # LLM
    openai_api_key: str = ""
    google_api_key: str = ""
    llm_provider: str = "openai"
    llm_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"

    # Paths
    vector_db_path: str = "data/processed/vector_db"
    raw_data_path: str = "data/raw"

    # App
    app_env: str = "development"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
