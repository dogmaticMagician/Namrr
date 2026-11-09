#!/bin/bash

uvicorn api:app --reload &

python3 main.py

kill$!