FROM python:3.8-alpine AS Builder
# Install dependencies
RUN pip install pipenv
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /code
# Copy sources files
WORKDIR /code
COPY . /code/
# Install migrations
RUN python manage.py makemigrations
RUN python manage.py migrate
# Run server
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]