FROM python:3-alpine

# Upgrade and install pip
RUN python -m pip install --upgrade pip

# Install make
RUN apk update && apk add make

# Create Working dir and copy requirements
WORKDIR /usr/local/app
COPY requirements.txt /usr/local/app/requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt

# Create appuser for running container as non root.
ENV USER=appuser
ENV UID=10001

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"
# Give app user access to work dir
RUN chown -R ${USER}: /usr/local/app
RUN chmod 755 /usr/local/app

# Copy code to the container
COPY . /usr/local/app

# Install klargest package locally
RUN python setup.py install

# Set app user as non root user
USER 10001