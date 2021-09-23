FROM python:3.7.4
RUN apt-get update && apt-get upgrade -y
COPY ./src_telegram /app
WORKDIR /app
RUN pip install -r requirements.txt
