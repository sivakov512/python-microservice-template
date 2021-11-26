recompile-proto:
	find proto -name "*.proto" | xargs -I {} \
	poetry run python -m grpc_tools.protoc \
		-I proto \
		--python_out=. \
		--grpc_python_out=. \
		--mypy_out=. \
		--mypy_grpc_out=. \
		{}

lint:
	poetry run flake8 ./
	poetry run mypy ./

test:
	poetry run pytest
