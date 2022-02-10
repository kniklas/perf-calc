lint:
	find . -name "*.py" | xargs python -m black -l 80 --check
	find . -name "*.py" | xargs python -m pylint
