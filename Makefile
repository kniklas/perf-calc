all: setup lint test

setup:
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
lint:
	find . -name "*.yml" | xargs python -m yamllint
	find . -name "*.py" | xargs python -m black -l 80 --check
	find . -name "*.py" | xargs python -m pylint

test:
	pytest
