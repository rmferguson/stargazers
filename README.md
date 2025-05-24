# Installation
You can install a project from another directory locally by aiming at it's wheel
```
(.venv) <PROJECT>>pip install ..\stargazers\dist\stargazers-x-py3-none-any.whl
```

or if you're using poetry, it knows how to find a wheel within a project.
```
poetry add ..\stargazers
```

# Working with Poetry
Installing a new dependency:
```
poetry add x
```

Installing a new development dependency:
```
poetry add x -D
```

Building the project for external usage:
```
poetry build --clean
```

Install the project (and it's dependencies):
```
poetry install
```

# On the code

TODO

# References

## Documentation
- [PEP-0000](https://peps.python.org/pep-0000/)
- [MyPy](https://mypy.readthedocs.io/en/stable/running_mypy.html)

## Blogs
- [Things I've learned about building CLI tools in Python](https://simonwillison.net/2023/Sep/30/cli-tools-python/)
- [Specifying entry points into a module](https://python-poetry.org/docs/pyproject/#entry-points)
- [Don't forget py.typed](https://blog.whtsky.me/tech/2021/dont-forget-py.typed-for-your-typed-python-package/)
- [Hard type hints for decorators](https://blog.whtsky.me/tech/2021/decorator-type-gymnastics-in-python/)
- [PyProject.toml](https://realpython.com/python-pyproject-toml/)

### Async
- [Async IO: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [AsyncIO - Awaitables, Tasks, and Futures](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-2)
- [Async Context Managers and Iterators](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-3.html)

## GitHub Curations
- [Awesome #Stuff](https://github.com/sindresorhus/awesome)

- [Vinta - Awesome Python](https://github.com/vinta/awesome-python)
- - [Awesome Python Typing](https://github.com/typeddjango/awesome-python-typing)

## Cool Stuff
- [Curio](https://github.com/dabeaz/curio)
- [Threado](https://github.com/dabeaz/thredo)

## To Read Libraries
A partial list of libraries and repos to look into.
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [DearPyGui](https://github.com/hoffstadt/DearPyGui)
- [PyAutoGUI](https://github.com/asweigart/pyautogui)
- [nicewin](https://github.com/asweigart/nicewin)
- [decouple](https://github.com/HBNetwork/python-decouple)
- [The Algoritms](https://github.com/TheAlgorithms/Python)
- [PyPattyrn](https://github.com/tylerlaberge/PyPattyrn)