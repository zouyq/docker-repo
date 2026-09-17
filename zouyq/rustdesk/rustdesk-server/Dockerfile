FROM rust:alpine AS builder

RUN apk add git alpine-sdk clang llvm musl-dev openssl-dev openssl-libs-static pkgconfig libsodium-dev

# Use the pinned hbb_common submodule; replacing it with latest breaks ed25519/signature versions
RUN git clone --depth 1 --recurse-submodules --shallow-submodules https://github.com/rustdesk/rustdesk-server.git
WORKDIR rustdesk-server

RUN cargo build --release --jobs=$(nproc)

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache libgcc

COPY --from=builder /rustdesk-server/target/release/rustdesk-utils /usr/local/bin/rustdesk-utils
COPY --from=builder /rustdesk-server/target/release/hbbr /usr/local/bin/hbbr
COPY --from=builder /rustdesk-server/target/release/hbbs /usr/local/bin/hbbs

WORKDIR /rustdesk
