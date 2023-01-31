
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


## Docker machine

```shell
$ docker-machine env wroom-prod
$ eval $(docker-machine env wroom-prod)

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
docker-compose -f docker-compose.yml run wroom python manage.py seed-db
docker-compose -f docker-compose.yml exec users-db psql -U postgres
```

```postgresql
\c users_dev
\dt
\q
```

## AWS
[//]: # (username: f****p****@g***.com)

### Install Docker
```shell
-- https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/
sudo yum install docker
sudo pip3 install docker-compose

sudo systemctl enable docker.service
sudo systemctl start docker.service
```

### SSH into shell
```shell
chmod 600 ~/.aws/key-pairs/wroom-f1-app.pem                                             
ssh -i ~/.aws/key-pairs/wroom-f1-app.pem ec2-user@ec2-<instance-ip>.amazonaws.com
```

### copy files over

```shell
rsync -av --exclude 'env' -e "ssh -i ~/.aws/key-pairs/wroom-f1-app.pem" wroom ubuntu@ec2-<instance-ip>.compute-1.amazonaws.com:/home/ubuntu 
```

## TODO
1. Hit API for drivers information and season information
2. Store in a text file, json