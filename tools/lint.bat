@echo off
autoflake -r -i .
isort .
black .
pylint --ignore-paths __pycache__/* build/* --disable C,R -- .