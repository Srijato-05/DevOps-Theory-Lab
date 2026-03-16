FROM postgres:16-alpine

# Copy custom postgresql.conf for performance tuning
COPY postgresql.conf /etc/postgresql/postgresql.conf

# Copy initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/

# Override the default command to use the custom config file
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
