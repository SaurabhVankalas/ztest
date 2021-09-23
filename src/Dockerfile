FROM python:3.7.4
RUN apt-get update && apt-get upgrade -y
COPY ./src /app
WORKDIR /app
RUN pip install -r requirements.txt
