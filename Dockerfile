FROM python:3-alpine

RUN python -m pip install --upgrade pip

ADD . /var/local/klargest

WORKDIR /var/local/klargest

RUN pip3 install -r requirements.txt

CMD ["/usr/local/bin/pytest", "-v -k 'not slowtest'"]
