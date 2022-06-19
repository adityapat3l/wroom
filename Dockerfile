FROM python:3.9

WORKDIR /app
ENV PYTHONPATH=/app

RUN apt-get -y update
RUN apt-get -y install git

COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt --upgrade --default-timeout=100

CMD python --version

