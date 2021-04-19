install:
	poetry install

brain_games:
	poetry run brain-games

brain_even:
	poetry run brain-even

brain_calc:
	poetry run brain-calc

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/hexlet_code-0.1.2-py3-none-any.whl

lint:
	poetry run flake8 brain_games
