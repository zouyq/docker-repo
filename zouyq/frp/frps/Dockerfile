FROM golang:alpine as builder

RUN apk add git

RUN git clone https://github.com/fatedier/frp.git
WORKDIR frp

RUN go build -o frps ./cmd/frps

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/frp/frps /usr/local/bin

ENTRYPOINT ["frps"]