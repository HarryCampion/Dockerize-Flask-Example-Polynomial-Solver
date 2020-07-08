#!/usr/bin/env bash

cd ../

docker build polynomial_solver -t polynomial_solver

docker run -d -p 5000:5000 polynomial_solver

echo "Visit http://0.0.0.0:5000/"
