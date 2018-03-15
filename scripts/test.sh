#!/bin/bash

# python tests
"${BASH_SOURCE%/*}/manage.sh" test

# python linter
flake8 .
