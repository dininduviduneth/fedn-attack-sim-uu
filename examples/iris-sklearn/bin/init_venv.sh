#!/bin/bash
set -e

# Init venv
python3 -m venv .mnist-pytorch

# Pip deps
.iris-sklearn/bin/pip install --upgrade pip
sudo .mnist-pytorch/bin/pip install -e ../../fedn
.iris-sklearn/bin/pip install -r requirements.txt