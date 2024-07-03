# Flask Health Check HTTP Server

Это простой HTTP-сервер на Flask, который возвращает статус "200 OK" на запрос `/healthz`.

1. Убедитесь, что у вас установлен Docker.
2. Перейдите в корневой каталог проекта:
    ```bash
    cd ci-cd/app
    ```
3. Постройте Docker-образ:
    ```bash
    docker build -t http_server .
    ```
4. Запустите контейнер:
    ```bash
    docker run -p 1337:1337 flask-healthz
    ```
5. Сервер будет запущен и доступен по адресу `http://localhost:1337/healthz`.

## Использование

Отправьте GET-запрос на `/healthz` для проверки состояния сервера:
```sh
curl http://localhost:1337/healthz
