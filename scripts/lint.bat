@echo off
echo Starting lint
FOR %%G IN (tests, src) DO (
    echo folder "%%G" start
    autoflake %%G -i -r --remove-unused-variables --remove-all-unused-imports --quiet > NUL 2>&1
    :: isort will format imports badly, so black has to be after.
    isort %%G > NUL 2>&1 
    black %%G > NUL 2>&1
    :: refurb %%G --ignore 112 --ignore 147 --quiet
    echo folder "%%G" done
)

echo Running pylint...
pylint -- .
mypy --strict-bytes --pretty -- src
pytest 
echo Finished lint