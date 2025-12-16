.PHONY: dev docker-dev

dev:
	uvicorn score.app:app --reload --host 0.0.0.0 --port 8000

docker-dev:
	docker build -f Dockerfile.dev -t score:latest .

start-score:
	docker run --rm -it -v $(shell pwd):/home/app/api -p 8000:8000 score
