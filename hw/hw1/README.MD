# Генериране на Docker image и стартиране на контейнер

## Създаване на Docker image
```
docker build -t <image_name> .
```

## Стартиране на контейнер
```
docker run -d -p 5001:5001 --name <container_name> <image_name>
```

## Проверка на работата на контейнера
```
docker ps
```

## Спиране на контейнера
```
docker stop <container_id>
```

## Премахване на контейнера
```
docker rm <container_id>
```

## Премахване на Docker image
```
docker rmi <image_name>
```
