#!/bin/bash

./setup.sh

if [ ! -f data/transactions.csv ]; then
    echo "Error: data/transactions.csv not found."
    exit 1
fi

TODAY=$(date +%Y-%m-%d)
REPORT_FILE="reports/report_$TODAY.txt"

python3 src/process.py data/transactions.csv "$REPORT_FILE"

TRANSACTION_COUNT=$(tail -n +2 data/transactions.csv | wc -l)

echo
echo "========== Nightly Summary =========="
echo "Transactions processed: $TRANSACTION_COUNT"

echo
echo "Flagged withdrawals:"

grep "Declined" "$REPORT_FILE" || echo "None"

echo
echo "Full report saved to:"
echo "$REPORT_FILE"
