from setuptools import setup,find_packages

setup(

    name="sample_repo",
    version=0.1,
    packages=find_packages(),
    install_requires=[
        "numpy>=1.11.1"
    ],
)