#!/bin/bash

rm -Rf venv/
virtualenv --python=python3.4 venv
source venv/bin/activate
pip3 install pyside
