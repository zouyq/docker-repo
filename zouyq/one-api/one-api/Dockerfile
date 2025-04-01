FROM golang:alpine AS builder

RUN apk add git npm
RUN git clone https://github.com/songquanpeng/one-api.git
WORKDIR /go/one-api/web/default

RUN npm install && npm run build

WORKDIR /go/one-api
RUN go build -ldflags "-s -w -X 'one-api/common.Version=$(cat VERSION)' -extldflags '-static'" -o one-api

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/one-api/one-api /usr/local/bin

ENTRYPOINT ["one-api"]