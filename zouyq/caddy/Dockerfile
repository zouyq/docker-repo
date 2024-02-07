FROM golang:alpine as builder

RUN apk add git
RUN git clone https://github.com/caddyserver/caddy.git
WORKDIR caddy

RUN go build -o caddy -a ./cmd/caddy

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/caddy/caddy /usr/local/bin

ENTRYPOINT ["caddy"]