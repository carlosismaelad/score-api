.PHONY: dev docker-build docker-dev up up-it logs stop start-score

DC := docker compose

dev:
	uvicorn score.app:app --reload --host 0.0.0.0 --port 8000

docker-build:
	$(DC) build

docker-dev:
	docker build -f Dockerfile.dev -t score:latest .

up:
	$(DC) up -d

up-it:
	$(DC) up

logs:
	$(DC) logs --follow

stop:
	$(DC) stop

start-score:
	docker run --rm -it -v $(shell pwd):/home/app/api -p 8000:8000 score
