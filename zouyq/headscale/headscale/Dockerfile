FROM golang:alpine as builder

RUN apk add git

RUN git clone https://github.com/juanfont/headscale.git
WORKDIR headscale

RUN go build -o headscale -a ./cmd/headscale

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/headscale/headscale /usr/local/bin

ENTRYPOINT ["headscale"]