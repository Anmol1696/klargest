PYTHON=python3
PIP=pip3

PYTEST_ARGS=-v -k
PYTEST_SLOW_FLAG=slowtest

DOCKER_IMAGE_NAME=klargest:latest
DOCKER_CONTAINER_NAME=klargest-container

.PHONY: test test-slow

all: run

install:
	$(PIP) install -r requirements.txt

test:
	pytest $(PYTEST_ARGS) "not $(PYTEST_SLOW_FLAG)"

test-slow:
	pytest $(PYTEST_ARGS) $(PYTEST_SLOW_FLAG)

run:
	$(PYTHON) -m klargest $(ARGS)

help:
	$(PYTHON) -m klargest --help


# Commands for docker setup and run
docker-build: docker-clear
	docker build . -t $(DOCKER_IMAGE_NAME)

docker-run:
	docker run -it --rm --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME) $(DOCKER_COMMAND)

docker-exec:
	$(MAKE) docker-run DOCKER_COMMAND=/bin/sh

docker-test:
	$(MAKE) docker-run DOCKER_COMMAND="/bin/sh -c \"pytest $(PYTEST_ARGS) 'not $(PYTEST_SLOW_FLAG)'\""

docker-test-slow:
	$(MAKE) docker-run DOCKER_COMMAND="/bin/sh -c \"pytest $(PYTEST_ARGS) $(PYTEST_SLOW_FLAG)\""

docker-clear-container:
	-docker rm $(DOCKER_CONTAINER_NAME)

docker-clear-image:
	-docker rmi $(DOCKER_IMAGE_NAME)

docker-clear: docker-clear-container docker-clear-image 