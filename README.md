# Invalid mypy issue

requirements: Docker, osx

```
docker-compose up -d

docker exec -it broken-mypy_py_1 bash

pip install mypy

mypy /root/app
```
