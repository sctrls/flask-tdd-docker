# pull official base image
FROM python:3.10.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# add app
COPY . .

# add entry point "entrypoint.sh"
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh