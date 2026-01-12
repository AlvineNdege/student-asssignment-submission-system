from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Student Assignment Submission System"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    
    # DB
    DATABASE_URL: str

    # Security
    SECRET_KEY: str="supersecretkey"
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    UPLOAD_DIR: str = "uploads"
    ADMIN_CODE: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
