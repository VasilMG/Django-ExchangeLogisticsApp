FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/el

WORKDIR $APP_HOME

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .


