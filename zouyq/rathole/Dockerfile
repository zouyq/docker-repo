FROM rust:alpine as builder

RUN apk add --no-cache git musl-dev openssl-dev pkgconfig perl make gcc

RUN git clone https://github.com/rapiz1/rathole.git
WORKDIR rathole

RUN cargo build --release --jobs=$(nproc)

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache libgcc

COPY --from=builder /rathole/target/release/rathole /usr/local/bin

ENTRYPOINT ["rathole"]