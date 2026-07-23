#!/bin/bash

CREDENTIAL_FILE="secrets/credentials.txt"
OUTPUT_FILE="secrets/operator.hash"


# Check if credential file exists
if [ ! -f "$CREDENTIAL_FILE" ]; then
    echo "Error: credentials.txt not found"
    exit 1
fi


# Extract operator ID
OPERATOR_ID=$(grep "operator_id" "$CREDENTIAL_FILE" | cut -d':' -f2 | xargs)


# Extract passphrase
PASSPHRASE=$(grep "passphrase" "$CREDENTIAL_FILE" | cut -d':' -f2 | xargs)


# Generate SHA-256 hash
HASH=$(echo -n "$PASSPHRASE" | sha256sum | awk '{print $1}')


# Store only ID and hash
echo "operator_id: $OPERATOR_ID" > "$OUTPUT_FILE"
echo "hash: $HASH" >> "$OUTPUT_FILE"


echo "Credential hash stored successfully."
echo "Saved to: $OUTPUT_FILE"
