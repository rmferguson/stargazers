@echo off
poetry update
poetry lock
poetry check && poetry sync && poetry build