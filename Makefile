PYTEST_ARGS=-v
PYTEST_SLOW_FLAG=slowtest
PYTHON=python3
PIP=pip3
DOCKER_IMAGE_NAME=klargest:latest
DOCKER_CONTAINER_NAME=klargest-container

.PHONY: test test-slow

all: run

install:
	$(PIP) install -r requirements.txt

test:
	pytest -k "not $(PYTEST_SLOW_FLAG)" $(PYTEST_ARGS)

test-slow:
	pytest -k $(PYTEST_SLOW_FLAG) $(PYTEST_ARGS)

run:
	$(PYTHON) -m klargest $(ARGS)

help:
	$(PYTHON) -m klargest --help

docker-build: docker-clear
	docker build . -t $(DOCKER_IMAGE_NAME)

docker-test: docker-clear-run
	docker run -it $(DOCKER_IMAGE_NAME)

docker-exec: docker-clear-run
	docker run -it --entrypoint "/bin/sh" --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

docker-clear: docker-clear-run
	-docker image rm $(DOCKER_IMAGE_NAME)

docker-clear-run:
	-docker rm $(DOCKER_CONTAINER_NAME)
