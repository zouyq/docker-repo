FROM golang:alpine as builder

RUN apk add git

RUN git clone https://github.com/fatedier/frp.git
WORKDIR frp

RUN go build -o frpc ./cmd/frpc

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/frp/frpc /usr/local/bin

ENTRYPOINT ["frpc"]