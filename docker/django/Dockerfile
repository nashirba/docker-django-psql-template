FROM python:3.8-slim-buster

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r /app/requirements.txt

# DATABASE starter
COPY ./docker/django/scripts/init_db /scripts/init_db
RUN sed -i 's/\r$//g' /scripts/init_db
RUN chmod +x /scripts/init_db

COPY ./docker/django/scripts/init_application /scripts/init_application
RUN sed -i 's/\r$//g' /scripts/init_application
RUN chmod +x /scripts/init_application

ENTRYPOINT ["/scripts/init_db"]
