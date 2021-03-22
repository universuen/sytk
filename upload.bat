pip install build
pip install twine
pip install wheel
python setup.py sdist bdist_wheel
twine upload dist/*
del /Q build
del /Q dist
del /Q sytk.egg-info