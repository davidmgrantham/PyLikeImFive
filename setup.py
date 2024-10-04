from setuptools import find_packages, setup

requirements = ["flask", "pygments"]

requirements_dev = [
    "flask",
    "pygments",
    "pytest",
    "pytest-cov",
    "pytest-html",
]

setup(
    name="pylikeimfive".strip("_"),
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
)
