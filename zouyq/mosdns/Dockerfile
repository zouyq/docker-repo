FROM golang:alpine AS builder

RUN apk add git

RUN git clone https://github.com/IrineSistiana/mosdns.git
WORKDIR mosdns

RUN go build  -o mosdns

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/mosdns/mosdns /usr/local/bin

ENTRYPOINT ["mosdns"]