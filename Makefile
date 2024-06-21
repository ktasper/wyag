test:
	 poetry run python -m pytest

fmt:
	poetry run isort .
	poetry run black .