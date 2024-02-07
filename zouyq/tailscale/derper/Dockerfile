FROM golang:alpine as builder

RUN apk add git

RUN git clone https://github.com/tailscale/tailscale.git
WORKDIR tailscale

RUN go build -o derper -a ./cmd/derper

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/tailscale/derper /usr/local/bin

ENTRYPOINT ["derper"]