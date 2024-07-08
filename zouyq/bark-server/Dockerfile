FROM golang:alpine AS builder

RUN apk add git

RUN git clone https://github.com/Finb/bark-server.git
WORKDIR bark-server

RUN go mod tidy && go build -o bark-server

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/bark-server/bark-server /usr/local/bin

ENTRYPOINT ["bark-server"]





