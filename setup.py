from setuptools import setup, find_packages

setup(
    name='AuthNex',
    version='0.1',
    author='Kuro-Raijin',
    author_email='sufyan532011@gmail.com',
    description='A login verification system for bots and games.',
    long_description=open('README.md').read(),
    long_description_content_type='IDK',
    url='https://github.com/RyomenSukuna53/AuthNex',  # your repo
    packages=find_packages(),
    install_requires=[
        'pyrogram',
        'tgcrypto',
        'tgcrypto',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.10',
)
