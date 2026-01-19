FROM golang:alpine AS builder

RUN apk add git npm
RUN git clone https://github.com/Calcium-Ion/new-api.git

# 前端构建使用 bun（避免 semi.css 问题）
FROM oven/bun:latest AS frontend-builder
WORKDIR /build
COPY --from=builder /go/new-api/web .
COPY --from=builder /go/new-api/VERSION .
RUN bun install
RUN DISABLE_ESLINT_PLUGIN='true' VITE_REACT_APP_VERSION=$(cat VERSION) bun run build

# 后端构建
FROM golang:alpine AS backend-builder
RUN apk add git
COPY --from=builder /go/new-api /go/new-api
WORKDIR /go/new-api
COPY --from=frontend-builder /build/dist ./web/dist
RUN go build -ldflags "-s -w -X 'new-api/common.Version=$(cat VERSION)' -extldflags '-static'" -o new-api

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=backend-builder /go/new-api/new-api /usr/local/bin

ENTRYPOINT ["one-api"]