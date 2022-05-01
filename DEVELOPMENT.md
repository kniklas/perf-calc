# Configure and use pyenv

1. Install [pyenv](https://github.com/pyenv/pyenv) on your computer.
2. Install [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) as pyenv plugin.
3. Install recommended Python v3.9.0 version: `pyenv install 3.9.0` (to see list of available versions invoke: `pyenv install --list`)
4. Create virtual environment based on installed 3.9.0 version: `pyenv virtualenv 3.9.0 your_env_name`

Then you can use your virtual environment and activate it using command: `pyenv activate your_env_name`.


# Use Makefile

* `make setup` - install all dependencies from `requirements.txt` file
* `make lint` - run linting checks for Python and Yaml and Black code formatting checks
* `make test` - execute unit tests and prints coverage report
* `make all` - run all above
