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
### [0.2.0] - 2018-10-05
#### Added
- `validateYAML` now accepts a loader parameter so that the faster CLoader parser can be used

### [0.1.5] - 2018-10-05
#### Added
- Python 3.6+ support!

#### Changed
- Uses click instead of codado.tx.Main for command-line parsing

#### Fixed
- Fixed command-line tool invocation
- Minor exception cleanup

### [0.1.4] - 2017-12-07
#### Changed
- Fixed issues in setup.py that were preventing package build

### [0.1.4] - 2017-12-07
#### Changed
- Fixed issues in setup.py that were preventing package build

### [0.1.3] - 2017-12-06
#### Added
- Added jsonschema dependency to setup

### [0.1.2] - 2017-12-05
#### Changed
- Minor stylistic updates

[0.2.0]: https://github.com/Brightmd/yamlschema/compare/release-0.1.5...release-0.2.0
[0.1.5]: https://github.com/Brightmd/yamlschema/compare/0.1.4...release-0.1.5
[0.1.4]: https://github.com/Brightmd/yamlschema/compare/0.1.3...0.1.4
[0.1.3]: https://github.com/Brightmd/yamlschema/compare/0.1.2...0.1.3
[0.1.2]: https://github.com/Brightmd/yamlschema/tree/0.1.2
