FROM golang:1.22-alpine as builder

RUN apk add git build-base

RUN git clone https://github.com/dolthub/dolt.git
WORKDIR dolt/go

RUN go build -o dolt -a ./cmd/dolt

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/dolt/go/dolt /usr/local/bin

ENTRYPOINT ["dolt"]





