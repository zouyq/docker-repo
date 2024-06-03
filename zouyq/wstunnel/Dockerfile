FROM rust:alpine as builder

RUN apk add git alpine-sdk

RUN git clone https://github.com/erebe/wstunnel.git
WORKDIR wstunnel

RUN cargo build --release --jobs=$(nproc)

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /wstunnel/target/release/wstunnel /usr/local/bin/wstunnel

ENTRYPOINT ["wstunnel"]