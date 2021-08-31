# Invalid mypy issue

requirements: Docker, osx

```
docker-compose up -d

docker exec -it broken-mypy_py_1 bash

pip install mypy

mypy /root/app
```


Issue

case insensitive folder in a docker bind mount in a linux container on a mac somehow
makes mypy loof for Activity.py and activity.py, and that's wrong.

```
root@f735f1a2f816:~/# mypy /root/app/
app/foo/bar/Activity.py:4: error: Module "app.f" has no attribute "FormTemplate"
app/foo/bar/activity.py:4: error: Module "app.f" has no attribute "FormTemplate"
app/f.py:3: error: Name "Activity" already defined (by an import)
app/__init__.py:2: error: Module "app.f" has no attribute "FormTemplate"
app/c.py:3: error: Module "app.f" has no attribute "FormTemplate"
Found 5 errors in 5 files (checked 7 source files)
```


Run without missing classes with invalid error (this is if you uncomment lines in f.py)

```
root@f735f1a2f816:/# mypy /root/app/
root/app/f.py:3: error: Name "Activity" already defined (by an import)
Found 1 error in 1 file (checked 7 source files) 
```
