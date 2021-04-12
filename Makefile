install:
	poetry install

brain_games:
	poetry run brain-games

brain_even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/hexlet_code-0.1.1-py3-none-any.whl

lint:
	poetry run flake8 brain_games
