python setup.py sdist bdist_wheel
twine upload dist/*
pip uninstall AuthNex.py -y
rm -rf build
rm -rf dist
rm -rf AuthNex.py.egg-info
