from setuptools import setup, find_packages

required_packages = [
    "beautifultable>=0.7.0",
    "dataclasses;python_version<'3.7'",
    "gpy==1.9.8",
    "gpyopt==1.2.5",
    "joblib>=0.13.2",
    "matplotlib>=3.0",
    "numpy>=1.16"
]

extras = {
    "tensorboard": ["tensorflow>=1.14.0", "tensorboard>=1.14.0"],
    "tests": ["pytest>=4.6.3", "pytest-timeout>=1.3.3"]
}

classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules"
]

setup(
    name="hypertunity",
    version="0.3.1",
    author="Georgi Dikov",
    author_email="gvdikov@gmail.com",
    url="https://github.com/gdikov/hypertunity",
    description="A toolset for distributed black-box hyperparameter optimisation.",
    long_description=open("README.md").read(),
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.6",
    install_requires=required_packages,
    extras_require=extras,
    classifiers=classifiers
)
