FROM debian:11-slim
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes libpython3-dev=3.9.2-3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# The URL of the messenger cluster
ENV MESSENGER_URL=nats://nats:4222

# The client-id of messenger
ENV MESSENGER_CLIENT_ID=person-service-python-impl

# The topic name
ENV SOME_TOPIC=some-topic

# Log level ['critical', 'error', 'warning', 'success', 'info', 'debug', 'trace']
ENV LOG_LEVEL=info

# The format of the log messages ['text', 'json']
ENV LOG_FORMAT=json

# Dump the actual configuration parameters of the application
ENV DUMP_CONFIG=False

COPY ./dist/cli /app

ENTRYPOINT ["/app"]
