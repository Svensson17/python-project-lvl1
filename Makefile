install:
	poetry install

brain_games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	poetry run flake8 brain_games
