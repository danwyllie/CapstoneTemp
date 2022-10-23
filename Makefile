setup:
    python3 -m venv ~/.CapstoneTemp

install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

test:
    python -m pytest -vv app.py

lint:
    pylint --disable=R,C app
	hadolint Dockerfile

all: install lint test