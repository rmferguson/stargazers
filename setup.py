from setuptools import find_packages, setup

pkg_name = "stargazers"
long_desc = """A longer description goes here."""

setup(
    name=pkg_name,
    description="Tools to help people shoot for the stars.",
    long_description=long_desc,
    author="Robert Ferguson",
    author_email="rmferguson@protonmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
