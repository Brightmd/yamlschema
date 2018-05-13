# Set variables

SHELL := /bin/bash

## Source files

MAIN_SRC_DIR = yamlschema
TESTS_SRC_DIR = yamlschema/test

MAIN_PYC_FILES := $(shell find $(MAIN_SRC_DIR) -name "*.pyc" -not -path "$(TESTS_SRC_DIR)/*")

## Test files

TESTS_PYC_FILES := $(shell find $(TESTS_SRC_DIR) -name "*.pyc")
TESTS_PYCACHE_FILES := $(shell find $(TESTS_SRC_DIR) -name "__pycache__")

#
# General targets
#

.DEFAULT_GOAL := all

.PHONY: all clean clean_all clean_dist clean_logs clean_pyc clean_tox sdist test wheel

all: clean test wheel

clean: clean_dist clean_logs clean_pyc

clean_all: clean clean_tox

clean_dist:
	-rm -r .Python env/ build/ develop-eggs/ dist/ eggs/ .eggs/ lib/ lib64/ parts/ sdist/ var/ *.egg-info/ .installed.cfg *.egg .eggs wheelhouse/*.whl

clean_logs:
	-rm $(shell find . -name '*.log')

clean_pyc:
	-rm -r $(MAIN_PYC_FILES) $(TESTS_PYC_FILES) $(TESTS_PYCACHE_FILES)

clean_tox:
	-rm -r .tox
	-rm -r .tox_output

sdist:
	python setup.py sdist

test:
	tox

wheel: clean_dist sdist
	python setup.py bdist_wheel
