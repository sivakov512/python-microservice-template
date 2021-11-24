import pytest

pytest_plugins = ["asyncpg_engine", "tests.factory"]

_config = {"POSTGRES_URL": "postgres://guest:guest@localhost:5432/guest?sslmode=disable"}


@pytest.fixture()
def config() -> dict[str, str]:
    return _config.copy()


@pytest.fixture()
def postgres_url(config: dict[str, str]) -> str:
    return config["POSTGRES_URL"]
