python -m slotscheck .
autoflake -r -i .
isort .
black .
refurb . 
pylint --ignore-paths __pycache__/* build/* --disable C,R -- .