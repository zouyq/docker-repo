FROM golang:1.26-alpine AS builder

RUN apk add --no-cache git

RUN git clone --depth 1 https://github.com/netbirdio/netbird.git
WORKDIR netbird

RUN go build -o netbird -a ./client

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/netbird/netbird /usr/local/bin

ENTRYPOINT ["netbird"]
CMD ["service", "run"]
