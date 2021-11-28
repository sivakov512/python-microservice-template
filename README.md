# Python microservice template

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to generate python grpc microservices.

Look at [generated service example](https://github.com/sivakov512/python-microservice-template-example) and [example protocol buffer repository](https://github.com/sivakov512/python-microservice-template-proto).

## What's included
* Nix shell configuration to start faster than anybody if you use [Nix](https://nixos.org/)
* [Poetry](https://github.com/python-poetry/poetry) to manage dependencies and all the Python staff
* Few [GRPC](https://grpc.io/docs/languages/python/quickstart/) and [protocol buffers](https://developers.google.com/protocol-buffers) related libs
* Great PostgreSQL driver [asyncpg](https://github.com/MagicStack/asyncpg) and pretty wrapper [asyncpg-engine](https://github.com/sivakov512/asyncpg-engine)
* [Click](https://github.com/pallets/click/) based cli
* Some linting staff, like [flake8](https://github.com/PyCQA/flake8) with a lot of plugins, [isort](https://github.com/PyCQA/isort), [mypy](https://github.com/python/mypy) and [black](https://github.com/psf/black) formatter (already configured!)
* [pytest](https://github.com/pytest-dev/pytest/) and some required plugins
* Nice pdb replacement [pdb++](https://github.com/pdbpp/pdbpp)
* Simple [helm](https://helm.sh/) chart to deploy to k8s
* Github Actions workflow with testing, releasing to Github Registry and deployment setup to [Yandex.Cloud](https://cloud.yandex.com/)

## Github Actions

Before using Github Actions you should add [PAT](https://github.com/settings/tokens) as secret named `ROBOT_TOKEN` (use special robot user, but personal token is okay too), otherwise CI will fail on git submodules checkout.

Also you should complete the following steps to deploy to Yandex.Cloud:
* Register at [Yandex.Cloud](https://cloud.yandex.com/) (it's a good service, really) and create k8s cluster
* Copy Kubernetes cluster ID to secret named `YANDEX_CLOUD_KUBERNETES_CLUSTER_ID`
* [Get IAM token for your Yandex.Cloud service account](https://cloud.yandex.ru/docs/iam/operations/iam-token/create-for-sa) and copy it (key.json content) to secret named `YANDEX_CLOUD_SERVICE_ACCOUNT_KEY`.

## Helm

Helm chart in repo is really very simple. You should edit it manually if you need some customization (and you need it).

## Database migrations

You can see that Github Actions, Dockerfile and k8s use [go-migrate](https://github.com/golang-migrate/migrate) tool to migrate database.
All existing migration tools are bad, but this tool is best of them. So it is my preferred choice.

## License

There are no LICENSE file in generated project, so add it yourself.
