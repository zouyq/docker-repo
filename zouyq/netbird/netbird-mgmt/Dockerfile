FROM golang:1.26-alpine AS builder

RUN apk add --no-cache git gcc musl-dev

# main currently fails to compile management (dex SQLite3.File mismatch);
# pin to the latest release so weekly rebuilds stay green.
ARG NETBIRD_VERSION=v0.78.2
RUN git clone --depth 1 --branch "${NETBIRD_VERSION}" https://github.com/netbirdio/netbird.git /netbird
WORKDIR /netbird

RUN go mod download
RUN CGO_ENABLED=1 go build -o /netbird-mgmt ./management

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /netbird-mgmt /usr/local/bin/netbird-mgmt

ENTRYPOINT ["netbird-mgmt"]
