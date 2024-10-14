#!/bin/bash

# Check if required environment variables are set
if [ "$POSTGRES_USER" != "cyuser" ]; then
  echo "Error: POSTGRES_USER is not 'cyuser'."
  exit 1
fi

if [ "$POSTGRES_PASSWORD" != "cloudyuga" ]; then
  echo "Error: POSTGRES_PASSWORD is not 'cloudyuga'."
  exit 1
fi

if [ "$POSTGRES_DB" != "cydb" ]; then
  echo "Error: POSTGRES_DB is not 'cydb'."
  exit 1
fi

# Initialize PostgreSQL
echo "PostgreSQL initialized with user: ${POSTGRES_USER}, password: [REDACTED], and database: ${POSTGRES_DB}"
