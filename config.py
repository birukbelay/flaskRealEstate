import os
from pathlib import Path

HERE = Path(__file__).parent
SQLITE_DEV = "sqlite:///" + str(HERE / "dev.db")
SQLITE_TEST = "sqlite:///" + str(HERE / "test.db")


uri = os.getenv("DATABASE_URL", SQLITE_DEV)
print("uri:--", uri)
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


class Config:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "open sesame")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    JSON_SORT_KEYS = False


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQLITE_TEST


class DevelopmentConfig(Config):
    """Development configuration."""
    TOKEN_EXPIRE_HOURS = 1
    TOKEN_EXPIRE_MINUTES = 15
    # SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_DATABASE_URI = os.getenv('LOCAL_POSTGRES_KEY')
    SECRET_KEY = os.getenv("SECRET_KEY", "open sesame")
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    TOKEN_EXPIRE_HOURS = 1

    SQLALCHEMY_DATABASE_URI = uri

    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = dict(
    dev=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)

