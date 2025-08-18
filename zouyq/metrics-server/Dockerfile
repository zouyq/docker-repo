FROM golang:alpine AS builder

RUN apk add git

RUN git clone https://github.com/kubernetes-sigs/metrics-server.git
WORKDIR metrics-server

RUN go build -o metrics-server ./cmd/metrics-server

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/metrics-server/metrics-server /usr/local/bin

ENTRYPOINT ["metrics-server"]