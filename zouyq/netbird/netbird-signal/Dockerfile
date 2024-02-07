FROM golang:alpine as builder

RUN apk add git

RUN git clone https://github.com/netbirdio/netbird.git
WORKDIR netbird

RUN go build -o netbird-signal -a ./signal

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/netbird/netbird-signal /usr/local/bin

ENTRYPOINT ["netbird-signal"]