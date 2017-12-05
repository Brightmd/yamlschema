# yamlschema

A schema validator for YAML files

## For maintainers: How to build

1. Increment `__version__` in `__version.py`.
2. Update the Change Log below.
3. Run the following:

```
python setup.py sdist bdist_wheel
twine upload dist/*<version>*
```

## Change Log

- 0.1.1 first working version