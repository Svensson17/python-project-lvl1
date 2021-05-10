install:
	poetry install

brain_games:
	poetry run brain-games

brain_even:
	poetry run brain-even

brain_calc:
	poetry run brain-calc

brain_gcd:
	poetry run brain-gcd

brain_progression:
	poetry run brain-progression

brain_prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/hexlet_code-0.1.5-py3-none-any.whl

lint:
	poetry run flake8 brain_games
