import os
import setuptools


# currentdir = os.getcwd()

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

with open("LICENSE", "r", encoding="utf-8") as f:
    license_str = f.read()

setuptools.setup(
    name="seamcorrector",
    version="1.0",
    author='Kaan Eraslan',
    python_requires='>=3.6.0',
    author_email="kaaneraslan@gmail.com",
    description="Marks seams and corrects them by dragging coordinates",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    license=license_str,
    url="https://github.com/D-K-E/SeamCorrector",
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*",
                 "docs", ".gitignore", "README.md"]
    ),
    test_suite="tests",
    install_requires=[
        "numpy",
        "scipy",
        "pillow",
        "PySide2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
