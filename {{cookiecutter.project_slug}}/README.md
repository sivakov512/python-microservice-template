# {{ cookiecutter.project_name }}
{{ cookiecutter.project_description }}

## Local development

### Installation and setup

First of all you should install Poetry using [official instructions](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) or solutions provided by your distro. Then install dependencies:
```bash
poetry install --no-root
```

### Lint and test

Project uses combination of `flake8`, `black`, `isort` and `mypy` for linting and `pytest` for testing.
Run them with `make`:

```bash
make lint
make test
```
