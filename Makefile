PYTHON := python3
PIP := pip3
LINTER := pylint

install:
	$(PIP) install --upgrade pip && \
		$(PIP) install -r requirements.txt

lint:
	$(LINTER) --disable=R,C /src/app/app.py

docker-build:
	docker build -t flask-app .

docker-run:
	docker run --rm -d -p 5000:5000 --name flask-app flask-app

docker-debug:
	docker run -d -p 5000:5000 --name flask-app flask-app
	docker exec -it flask-app /bin/bash

docker-stop:
	docker rm -f flask-app

docker-clean:
	docker rm -f flask-app
	docker rmi -f flask-app
