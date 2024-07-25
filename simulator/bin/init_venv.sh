#!/bin/bash
set -e

# Init venv
python3 -m venv .simulator

# Pip deps
.simulator/bin/pip install --upgrade pip
sudo .simulator/bin/pip install -e ../fedn
sudo .simulator/bin/pip install -r requirements.txt
