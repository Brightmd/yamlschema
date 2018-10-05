"""
Validate a YAML file
"""
from __future__ import print_function

import sys

import yaml

import click

from jsonschema import validate, FormatChecker


@click.command()
@click.argument('yamlfile', type=click.File())
@click.argument('yamlschema', type=click.File())
def validateYAMLCLI(yamlfile, yamlschema):
    print("Validating {}\n".format(yamlfile.name), file=sys.stderr)
    validateYAML(yamlfile, yamlschema)
    print("{} is valid\n".format(yamlfile.name), file=sys.stderr)


def validateYAML(yamlFile, yamlSchema):
    """
    Validate yaml file based off of a schema
    """
    contents = yaml.load(yamlFile)
    schema = yaml.load(yamlSchema)
    validate(contents, schema, format_checker=FormatChecker())
    return True
