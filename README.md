# What the function is this?

Stargazers is a module of stuff that I frequently find myself repackaging and using for the same personal projects. Now instead of writing the code again, I just put it in Stargazers.

Eventually I decided I conceded to the vague notion of "doing this right", repackaged it all as a Poetry project, annotated almost every single bit of code, and decided to open source it. As much as I don't really like the idea of code I wrote being used to train AI Slop™, at least if there's good code in the training data, then maybe it won't be quite so Slop™. That said, I would really prefer you do not train your model on my code.

I attempted to most of the swearing and some of the snark during this refactor. I will not remove all of it.

There are some mildly interesting batch scripts in... `\scripts` as well that I use during hobbyist development. They're really just there to provide a facsimile of a build system, and to make activating a Poetry virtual environment less of a pain in the butt on Windows 10.

# References

## Documentation
- [PEP-0000](https://peps.python.org/pep-0000/)
- [MyPy](https://mypy.readthedocs.io/en/stable/running_mypy.html)

## Blogs/How-Tosc
- [Don't forget py.typed](https://blog.whtsky.me/tech/2021/dont-forget-py.typed-for-your-typed-python-package/)
- [Hard type hints for decorators](https://blog.whtsky.me/tech/2021/decorator-type-gymnastics-in-python/)
- [PyProject.toml - RealPython.com](https://realpython.com/python-pyproject-toml/)
- [Things I've learned about building CLI tools in Python](https://simonwillison.net/2023/Sep/30/cli-tools-python/)
- [Specifying entry points into a module](https://python-poetry.org/docs/pyproject/#entry-points)
- [Packaging Entry Points - Click](https://click.palletsprojects.com/en/stable/entry-points/)
- [How and Why to write Copyright in your code](https://liferay.dev/blogs/-/blogs/how-and-why-to-properly-write-copyright-statements-in-your-code)

### Async
- [Async IO: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [AsyncIO - Awaitables, Tasks, and Futures](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-2)
- [Async Context Managers and Iterators](https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-3.html)

## My "Awesome" Curations
- [Curio - Async from the ground up](https://github.com/dabeaz/curio)
- [Threado - Threads and Async, together at last...?](https://github.com/dabeaz/thredo)
- [Whenever - Datetime for the modern man](https://github.com/ariebovenberg/whenever)
- [Click - Can't spell CLI without Click](https://click.palletsprojects.com/en/stable/)
- [Falyx - Click but Edgy and Async](https://pypi.org/project/falyx/)

## Other GitHub Curations
- [Awesome #Stuff](https://github.com/sindresorhus/awesome)
- [Vinta - Awesome Python](https://github.com/vinta/awesome-python)
- - [typeddjango - Awesome Python Typing](https://github.com/typeddjango/awesome-python-typing)


# Legal Stuff
### MIT License

Copyright (c) 2025 Robert Ferguson <rmferguson@pm.me>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the " Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


### Additional
In an attempt to reinforce the license above, you will see the following in the doc string of every file:
> ### Legal
> SPDX-FileCopyright © 2025 Robert Ferguson <rmferguson@pm.me>
> 
> SPDX-License-Identifier: MIT

