#!/bin/bash

mkdir -p ui/
venv/bin/python venv/lib/python3.4/site-packages/PySide/scripts/uic.py -o ui/MainWindowView.py res/ui/MainWindow.ui
