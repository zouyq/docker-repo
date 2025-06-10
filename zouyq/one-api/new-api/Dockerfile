FROM golang:alpine AS builder

RUN apk add git npm
RUN git clone https://github.com/Calcium-Ion/new-api.git
WORKDIR /go/new-api/web

RUN npm install --force && npm run build

WORKDIR /go/new-api
RUN go build -ldflags "-s -w -X 'one-api/common.Version=$(cat VERSION)' -extldflags '-static'" -o one-api

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/new-api/one-api /usr/local/bin

ENTRYPOINT ["one-api"]