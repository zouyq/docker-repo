FROM golang:alpine as builder

RUN apk add git

RUN git clone https://github.com/tailscale/tailscale.git
WORKDIR tailscale

RUN go build -o tailscale -a ./cmd/tailscale
RUN go build -o tailscaled -a ./cmd/tailscaled

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache ca-certificates iptables iproute2 ip6tables tzdata

COPY --from=builder /go/tailscale/tailscale /usr/local/bin
COPY --from=builder /go/tailscale/tailscaled /usr/local/bin

ENTRYPOINT ["tailscaled"]