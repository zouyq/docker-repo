FROM rust:alpine AS builder

RUN apk add git alpine-sdk clang llvm

RUN git clone https://github.com/rustdesk/rustdesk-server.git
WORKDIR rustdesk-server

RUN rm -rf libs && git clone https://github.com/rustdesk/hbb_common.git libs/hbb_common

RUN cargo build --release --jobs=$(nproc)

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache libgcc

COPY --from=builder /rustdesk-server/target/release/rustdesk-utils /usr/local/bin/rustdesk-utils
COPY --from=builder /rustdesk-server/target/release/hbbr /usr/local/bin/hbbr
COPY --from=builder /rustdesk-server/target/release/hbbs /usr/local/bin/hbbs

WORKDIR /rustdesk