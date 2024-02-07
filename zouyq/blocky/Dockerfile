FROM golang:alpine as builder

RUN apk add git

RUN git clone https://github.com/0xERR0R/blocky.git
WORKDIR blocky

RUN go build -o blocky

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/blocky/blocky /usr/local/bin

ENTRYPOINT ["blocky"]





