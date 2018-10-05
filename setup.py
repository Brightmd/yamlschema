from inspect import cleandoc

from setuptools import setup


_version = {}
exec(open('yamlschema/_version.py').read(), _version)


setup(
  name = 'yamlschema',
  packages = ['yamlschema', 'yamlschema.test'],
  version = _version['__version__'],
  description = 'A schema validator for YAML files',
  author = 'Ashley Fisher',
  author_email = 'fish.ash@gmail.com',
  url = 'https://github.com/Brightmd/yamlschema',
  keywords = ['yaml', 'schema'],
  classifiers = [],
  scripts = ['bin/yamlschema'],
  install_requires=cleandoc('''
    click>=5.0,<8.0
    jsonschema==2.6.0
    ''').split()
)
