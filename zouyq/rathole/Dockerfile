FROM rust as builder

RUN git clone https://github.com/rapiz1/rathole.git
WORKDIR rathole

RUN cargo build --release --jobs=$(nproc)

FROM zouyq/wolfi
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /rathole/target/*/release/rathole /usr/local/bin/rathole

ENTRYPOINT ["rathole"]
