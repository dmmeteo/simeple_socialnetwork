# simple Social Network

## How to start

To up services, just run docker-compose inside root directory with docker-compose.yml. E.g.:
```sh
docker-compose up
```

To run automated bot:
```sh
docker-compose run --rm ./runner.py
```

## Sevices

To see what's going out:

* Swagger UI of api: http://localhost:8000/docs/
* Flower UI of Celery: http://localhost:5000/
