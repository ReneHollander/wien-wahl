#!/bin/bash

function gen {
  pyside-uic -o ui/$1View.py res/ui/$1.ui
  echo $1
}

mkdir -p ui/

gen Import
gen Main
