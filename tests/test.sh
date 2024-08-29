#!/bin/bash

# Set the module name where your tests are located
MODULE_NAME="tests/test_model.py"

# Run pytest with the specified module
pytest $MODULE_NAME

# Verbose command
# pytest $MODULE_NAME --verbose --maxfail=1 --disable-warnings
