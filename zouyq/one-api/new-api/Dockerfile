FROM oven/bun:1.4-alpine AS frontend-builder

RUN apk add --no-cache git
RUN git clone --depth 1 --recurse-submodules https://github.com/zyqfork/new-api.git /new-api

WORKDIR /new-api/web
RUN bun install --frozen-lockfile
RUN DISABLE_ESLINT_PLUGIN='true' VITE_REACT_APP_VERSION=$(cat /new-api/VERSION) bun run build

FROM golang:1.26-alpine AS backend-builder

RUN apk add --no-cache git
COPY --from=frontend-builder /new-api /new-api
WORKDIR /new-api

ENV CGO_ENABLED=0
RUN go build -ldflags "-s -w -X 'github.com/QuantumNous/new-api/common.Version=$(cat VERSION)'" -o /new-api-bin

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=backend-builder /new-api-bin /usr/local/bin/new-api

ENTRYPOINT ["new-api"]
