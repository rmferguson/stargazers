# Installation
`(.venv) <PROJECT>>pip install ..\stargazers\dist\stargazers-x-py3-none-any.whl`
or
`poetry add ..\stargazers`

# Working with Poetry
Installing a new dependency:

```poetry add x```

Installing a new development dependency:

```poetry add x -D```

Building the project for external usage:

```poetry build --clean```

Install the project (and it's dependencies):

```poetry install```


# References
- [Things I've learned about building CLI tools in Python](https://simonwillison.net/2023/Sep/30/cli-tools-python/)
- [Specifying entry points into a module](https://python-poetry.org/docs/pyproject/#entry-points)
- [AsyncIO - Awaitables, Tasks, and Futures](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-2)
- [Async Context Managers and Iterators](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-3.html)

## Libraries
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)