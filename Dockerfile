#Pull the official base image
FROM python:3.9

#set work directory
WORKDIR /code

#set environment variables
ENV PYTHONUNBUFFERED=1

#install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

#copy project
COPY . /code/