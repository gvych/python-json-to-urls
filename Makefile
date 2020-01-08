all:
#	pip install -r requirements.txt
	./main.py ./data.json

setup:
	virtualenv --python=python3 .env
	source .env/bin/activate
	pip install -r requirements.txt

