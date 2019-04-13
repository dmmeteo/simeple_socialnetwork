o "Waiting for postgres..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Migrates the database, uploads staticfiles, and runs the production server
./manage.py makemigrations && \
./manage.py migrate && \
./manage.py collectstatic --noinput && \
gunicorn --bind 0.0.0.0:$PORT  --log-file - socialnetwork.config.wsgi:application
