@echo off
FOR %%G IN (tests, src) DO (
    echo folder "%%G" start
    autoflake %%G -i -r --remove-unused-variables --remove-all-unused-imports --quiet > NUL 2>&1
    :: isort can format imports badly, so black has to be after.
    isort %%G > NUL 2>&1 
    black %%G > NUL 2>&1
)

pylint -- tests src
mypy --strict-bytes --pretty -- src
pytest 
