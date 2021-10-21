all: install

install:
	python setup.py install

test :
	black .
	flake8 . --statistics
	python -m pytest --pyargs --doctest-modules altair_examples

test-coverage:
	python -m pytest --pyargs --doctest-modules --cov=altair_examples --cov-report term altair_examples

test-coverage-html:
	python -m pytest --pyargs --doctest-modules --cov=altair_examples --cov-report html altair_examples
