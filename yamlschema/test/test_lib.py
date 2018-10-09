"""
Tests for YAML file validation
"""
import re

from jsonschema import ValidationError

from click.testing import CliRunner

from codado import fromdir

from pytest import fixture

from yamlschema import lib


@fixture
def runner():
    return CliRunner()


@fixture
def schemaFile():
    return fromdir(__file__)('test_config.schema.yml')


@fixture
def configGood():
    return fromdir(__file__)('test_config.yml')


@fixture
def configBad():
    return fromdir(__file__)('test_config_bad.yml')


def test_validateConfigOK(runner, schemaFile, configGood):
    """
    Does a good config pass?
    """
    x = runner.invoke(lib.validateYAMLCLI, [configGood, schemaFile])
    assert x.exception is None
    assert x.exit_code == 0
    assert re.search(r'%s is valid' % configGood, x.output)


def test_validateConfigBad(runner, schemaFile, configBad):
    """
    Does a bad config fail?
    """
    x = runner.invoke(lib.validateYAMLCLI, [configBad, schemaFile])
    assert isinstance(x.exception, ValidationError)


def test_validateYAMLWithFilename(schemaFile, configGood):
    """
    Can you invoke validateYAML with a filename as well as an open file?
    """
    assert lib.validateYAML(schemaFile, configGood)
