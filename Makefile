all: setup lint test clean

setup:
	@echo "Starting setup"
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
	@echo "Completed setup"
lint:
	@echo "Starting lint"
	find . -name "*.yml" | xargs python -m yamllint
	find . -name "*.py" | xargs python -m black -l 80 --check
	find . -name "*.py" | xargs python -m pylint
	@echo "Completed lint"

test:
	pytest

clean:
	@echo "Starting clean"
	find . -name ".pytest_cache" -o  -name "__pycache__" | xargs rm -rfv
	@echo "Completed clean"
