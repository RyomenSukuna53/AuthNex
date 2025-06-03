from setuptools import setup, find_packages
import re

with open("requirements.txt", encoding="utf-8") as mano:
  requires = [z.strip() for z in mano]
    
with open("AuthNex/__init__.py", encoding="utf-8") as fk:
  version = "1.0.0"

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
