@echo off
poetry update
poetry lock
poetry check --strict && poetry sync --compile --all-groups && poetry build --clean
