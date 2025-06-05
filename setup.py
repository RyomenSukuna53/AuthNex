from setuptools import setup, find_packages
import re

with open("README.md", "r") as f:
        description = f.read()
setup( 
  name="AuthNex",
  version='0.1[BETA]',
  packages=find_packages(),
  install_requires=requires,
  author="Kuro__",
  author_email="sufyan532011@gmail.com",
  description="just a try",
  long_description=description,
  long_description_content_type="text/markdown",
  url="https://github.com/RyomenSukuna53/AuthNex",
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.10',
)
