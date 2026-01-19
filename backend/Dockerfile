FROM python:3.12-bookworm

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY ./requirements.txt tmp/requirements.txt
RUN pip install -r tmp/requirements.txt

RUN mkdir /django_app
WORKDIR /django_app
COPY . /django_app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /django_app
USER appuser
CMD ["ls"]
CMD ["python", "manage.py", "runserver"]