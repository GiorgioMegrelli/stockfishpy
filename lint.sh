#!/bin/bash

# Check packages
python3 -m pip install -r dev-requirements.txt

for inp in "$@"; do
    python3 -m black $inp
    python3 -m isort $inp
done
