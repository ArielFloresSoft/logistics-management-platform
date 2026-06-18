from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
app_name: str = "Logistics Management Platform API"
app_env: str = "development"

```
api_v1_prefix: str = "/api/v1"

database_url: str
redis_host: str = "redis"
redis_port: int = 6379

secret_key: str
access_token_expire_minutes: int = 30

cors_origins: list[str] = ["http://localhost:5173"]

model_config = SettingsConfigDict(
    env_file=".env",
    case_sensitive=False,
    extra="ignore"
)
```

settings = Settings()
