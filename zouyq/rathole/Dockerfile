FROM rust:alpine as builder

ARG TARGETPLATFORM

RUN apk add --no-cache git musl-dev openssl-dev openssl-libs-static pkgconfig perl make gcc

RUN git clone https://github.com/rapiz1/rathole.git
WORKDIR rathole

ENV RUSTFLAGS="-C target-feature=-outline-atomics"

# 根据目标平台设置 Rust target
RUN case "${TARGETPLATFORM}" in \
    "linux/amd64") export RUST_TARGET="x86_64-unknown-linux-musl" ;; \
    "linux/arm64") export RUST_TARGET="aarch64-unknown-linux-musl" ;; \
    "linux/arm/v7") export RUST_TARGET="armv7-unknown-linux-musleabihf" ;; \
    "linux/386") export RUST_TARGET="i686-unknown-linux-musl" ;; \
    "linux/ppc64le") export RUST_TARGET="powerpc64le-unknown-linux-musl" ;; \
    *) echo "Unsupported platform: ${TARGETPLATFORM}" && exit 1 ;; \
    esac && \
    rustup target add ${RUST_TARGET} && \
    cargo build --release --target ${RUST_TARGET}

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /rathole/target/*/release/rathole /usr/local/bin/rathole

ENTRYPOINT ["rathole"]
