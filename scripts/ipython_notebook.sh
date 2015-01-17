#!/bin/bash

ROOT_DIR=/vagrant
export PYTHONPATH=$ROOT_DIR/python:/vagrant/vincent

IPYTHON_CMD="ipython notebook --port=8888 --ip=0.0.0.0 --no-browser"

NOTEBOOKS_DIR=$ROOT_DIR/notebooks

$IPYTHON_CMD --notebook-dir=$NOTEBOOKS_DIR

