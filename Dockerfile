# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app .

RUN mkdir -p app/static

COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["uwsgi", "app_uwsgi.ini"]
