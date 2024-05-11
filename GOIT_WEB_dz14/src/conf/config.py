from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = 'SQLALCHEMY_DATABASE_URL'
    secret_key: str = 'SECRET_KEY'
    algorithm: str = 'ALGORITHM'
    mail_username: str = 'MAIL_USERNAME'
    mail_password: str = 'MAIL_PASSWORD'
    mail_from: str = 'MAIL_FROM'
    mail_port: int = 465
    mail_server: str = 'MAIL_SERVER'
    redis_host: str = 'localhost'
    redis_port: int = 6379
    cloudinary_name: str = 'CLOUDINARY_NAME'
    cloudinary_api_key: str = 'CLOUDINARY_API_KEY'
    cloudinary_api_secret: str = 'CLOUDINARY_API_SECRET'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()