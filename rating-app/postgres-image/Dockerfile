# Use the official PostgreSQL image
FROM postgres:latest

# Add an initialization script to verify the environment variables
COPY init.sh /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432
