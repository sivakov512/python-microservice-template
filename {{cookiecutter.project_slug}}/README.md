# {{ cookiecutter.project_name }}
{{ cookiecutter.project_description }}

## Local development

### Installation and setup

First of all you should install Poetry using [official instructions](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) or solutions provided by your distro. Then install dependencies:
```bash
poetry install --no-root
```

Run PostgreSQL using provided docker-compose configuration:
```bash
docker-compose up  # run it in another terminal or add `-d` to daemonize
```

Now install [migrate CLI](https://github.com/golang-migrate/migrate/tree/master/cmd/migrate#installation) to work with database migrations and migrate database:
```bash
migrate -database "postgres://guest:guest@localhost:5432/guest?sslmode=disable" -path migrations up
```

Compile protocol buffers:
```bash
make recompile-proto
```

### Lint and test

Project uses combination of `flake8`, `black`, `isort` and `mypy` for linting and `pytest` for testing.
Run them with `make`:

```bash
make lint
make test
```
