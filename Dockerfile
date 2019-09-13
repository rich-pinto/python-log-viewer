FROM ubuntu:16.04

MAINTAINER Richard Pinto "richardpinto87@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev less

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
