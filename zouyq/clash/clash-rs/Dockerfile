FROM node AS frontend

RUN git clone https://github.com/haishanh/yacd.git
WORKDIR /yacd

RUN npm -g install pnpm
RUN pnpm install && pnpm build

FROM rust AS backend
RUN apt update -y && apt install -y protobuf-compiler

RUN git clone https://github.com/Watfaq/clash-rs.git
WORKDIR /clash-rs

RUN cargo build --release --jobs=$(nproc)

FROM ubuntu

COPY --from=frontend /yacd/public /ui
COPY --from=backend /clash-rs/target/release/clash-rs /usr/local/bin/

ENTRYPOINT ["clash-rs"]
