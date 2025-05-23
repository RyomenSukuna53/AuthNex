python setup.py sdist bdist_wheel
twine upload dist/*
pip uninstall AuthNex -y
rm -rf build
rm -rf dist
rm -rf AuthNex.egg-info
