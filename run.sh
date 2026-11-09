#!/bin/bash

uvicorn api:app --reload --log-level critical &

python3 main.py

kill$!