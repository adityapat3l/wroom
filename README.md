
# Getting Started

For M1 Macs:
```shell
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```

## F1-app
```
docker-compose build f1-app
docker-compose run --rm f1-app
python main.py
```

## Getting all the servies up

```
docker-compose -f docker-compose.yml up -d --build
```


## Working with app and db in shell
```
docker-compose -f docker-compose.yml run wroom flask shell

>>> app
>>> db
>>> exit()
```


## Test & Logs
```
docker-compose -f docker-compose.yml run wroom pytest
docker-compose -f docker-compose.yml logs
```
OR
```
docker-compose -f docker-compose.yml run wroom python manage.py test
```

## DB

Recreate DB and hop into postgres
```shell
docker-compose -f docker-compose.yml run wroom python manage.py recreate-db
docker-compose -f docker-compose.yml exec users-db psql -U postgres
```

```postgresql
\c users_dev
\dt
\q
```

## TODO
1. Hit API for drivers information and season information
2. Store in a text file, json