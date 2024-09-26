from setuptools import find_packages, setup

requirements = ["python-fasthtml", "pyyaml"]

requirements_dev = [
    "flask",
    "pytest",
    "pytest-cov",
    "pytest-html",
    "python-fasthtml",
    "pyyaml",
]

setup(
    name="pylikeimfive".strip("_"),
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
)
