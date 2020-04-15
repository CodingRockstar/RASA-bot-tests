# RASA CLI commands

## RASA actions (local)

Start actions server first. 

```
rasa run actions -vv
```

## RASA server (local)

On CLI for debug

```
rasa shell --debug --endpoints endpoints.yml -vv --enable-api --cors "*"
```

As server

```
rasa run --m ./models --endpoints endpoints.yml -vv --enable-api --cors "*"
```

As server with debug

```
rasa run --m ./models --endpoints endpoints.yml -vv --enable-api --cors "*" --debug
```


## RASA X - Server

get all kubernetes pods

```
kubectl get pods
```

get logs for one special pod

```
kubectl logs rasa-app-56bbfc988-wkzgz
```

delete one pod

```
kubectl delete pod rasa-event-service-bd46f7594-f4px4
```


## RASA X - Deploy Actions Server

create Docker image for actions server

```
docker build . -t codingrockstar/rasa-gbll-bot-action:202004152002
```

upload to dockerhub

```
docker login --username codingrockstar --password 'xxx'
```

```
docker push codingrockstar/rasa-gbll-bot-action:202004152002
```

deploy on RASA X server

```
export ACTION_SERVER_IMAGE="codingrockstar/rasa-gbll-bot-action"
```

```
export ACTION_SERVER_TAG="202004131847"
```

```
curl -s get-rasa-x.rasa.com | sudo -E bash
```