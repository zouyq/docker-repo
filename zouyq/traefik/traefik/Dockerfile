FROM golang:alpine AS builder

RUN apk add --no-cache git go gcc musl-dev

RUN git clone https://github.com/traefik/traefik.git
WORKDIR traefik

RUN go build -o traefik -a ./cmd/traefik

FROM alpine
LABEL MAINTAINER="zyqcn@live.com"

COPY --from=builder /go/traefik/traefik /usr/local/bin

ENTRYPOINT ["traefik"]


