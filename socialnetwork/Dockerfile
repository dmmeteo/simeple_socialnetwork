FROM python:3.7
ENV PYTHONUNBUFFERED 1


# Adds our application code to the image
COPY . /code/
WORKDIR /code

# Allows docker to cache installed dependencies between builds
RUN pip install pipenv
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    gunicorn --bind 0.0.0.0:$PORT  --log-file - socialnetwork.config.wsgi:application
