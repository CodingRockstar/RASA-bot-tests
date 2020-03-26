# RASA CLI commands

## RASA actions

Start actions server first. 

```
rasa run actions -vv
```

## RASA server

On CLI for debug

```
rasa shell --debug --enable-api --cors "*"
```

As server

```
rasa run --m ./models --endpoints endpoints.yml -vv --enable-api --cors "*"
```

As server with debug

```
rasa run --m ./models --endpoints endpoints.yml -vv --enable-api --cors "*" --debug
```