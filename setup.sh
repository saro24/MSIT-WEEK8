#!/bin/bash

echo "===================================="
echo " TartanBank Project Setup"
echo "===================================="
echo

mkdir -p data
mkdir -p reports
mkdir -p src
mkdir -p secrets

echo "data folder ready"
echo "reports folder ready"
echo "src folder ready"
echo "secrets folder ready"

echo

if [ -f "data/transactions.csv" ]; then
    echo "transactions.csv found."
else
    echo "WARNING: data/transactions.csv is missing."
    echo "Please copy transactions.csv into the data folder."
fi

echo
echo "Project setup complete."
