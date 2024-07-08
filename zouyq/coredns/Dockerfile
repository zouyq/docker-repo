FROM golang:alpine AS builder

RUN apk add git

RUN git clone https://github.com/coredns/coredns.git
WORKDIR coredns

RUN go build -o coredns

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/coredns/coredns /usr/local/bin

ENTRYPOINT ["coredns"]