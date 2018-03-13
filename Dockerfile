FROM python:3-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN apk update && \
 apk add postgresql-libs postgresql-client && \
 apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /code/

EXPOSE 8222
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
