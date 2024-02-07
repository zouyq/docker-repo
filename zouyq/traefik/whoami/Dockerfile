FROM golang:alpine as builder

RUN apk add git go gcc musl-dev

RUN git clone https://github.com/traefik/whoami.git
WORKDIR whoami

RUN go build -o whoami

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/whoami/whoami /usr/local/bin

ENTRYPOINT ["whoami"]


