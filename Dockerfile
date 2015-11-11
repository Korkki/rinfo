FROM python:3.5
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update -y && apt-get install -y \
    postgresql-server-dev-9.4
ADD requirements.txt /code/
ADD . /code/
RUN pip install -r requirements/dev.txt
RUN useradd rav
USER rav