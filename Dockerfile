FROM python:3-alpine

RUN python -m pip install --upgrade pip

WORKDIR /usr/local/app
COPY requirements.txt /usr/local/app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /usr/local/app