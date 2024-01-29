
import os


def _get_env(key: str):
    env = os.getenv(key)
    if env is None:
        return env

    if env.strip() == "":
        os.environ.pop(key)
        return None

    return env

class Env:
    DATABASE_HOST = _get_env("DATABASE_HOST")
    DATABASE_PORT = _get_env("DATABASE_PORT")
    DATABASE_NAME = _get_env("DATABASE_NAME")
    DATABASE_USER = _get_env("DATABASE_USER")
    DATABASE_PASSWORD = _get_env("DATABASE_PASSWORD")