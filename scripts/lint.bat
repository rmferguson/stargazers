@echo off
autoflake src\stargazers -i -r --remove-unused-variables --remove-all-unused-imports --quiet
:: isort will format imports badly, so black has to be after.
isort . && black .
refurb src\stargazers --ignore 112 --quiet
pylint -- src\stargazers