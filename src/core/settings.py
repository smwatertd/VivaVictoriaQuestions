from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    name: str = 'FastAPI'
    host: str = '0.0.0.0'
    port: int = 8000

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='APP_',
    )


class DatabaseSettings(BaseSettings):
    driver: str = 'postgresql+asyncpg'
    options: str = '?async_fallback=True'
    host: str = 'localhost'
    port: int = 5432
    user: str = 'postgres'
    password: str = 'postgres'
    database: str = 'postgres'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='DB_',
    )

    @property
    def url(self) -> str:
        return f'{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}{self.options}'


app_settings = AppSettings()
db_settings = DatabaseSettings()
