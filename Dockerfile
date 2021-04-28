FROM python:3-alpine

# Upgrade and install pip
RUN python -m pip install --upgrade pip

# Create Working dir and copy requirements
WORKDIR /usr/local/app
COPY requirements.txt /usr/local/app/requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt

# Copy code to the container
COPY . /usr/local/app

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

USER 10001