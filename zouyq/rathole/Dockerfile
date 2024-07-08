FROM rust AS builder

RUN git clone https://github.com/rapiz1/rathole.git
WORKDIR rathole

RUN cargo build --release --jobs=$(nproc)

FROM alpine:edge
LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache gcompat

COPY --from=builder /rathole/target/release/rathole /usr/local/bin

ENTRYPOINT ["rathole"]