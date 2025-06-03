from setuptools import setup, find_packages
import re


setup( 
  name="AuthNex",
  version=version,
  packages=find_packages(),
  install_requires=requires,
  author="Kuro__",
  author_email="sufyan532011@gmail.com",
  description="just a try",
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  url="https://github.com/RyomenSukuna53/AuthNex",
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.12',
)
