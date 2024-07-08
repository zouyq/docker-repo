FROM node as frontend

RUN git clone https://github.com/haishanh/yacd.git
WORKDIR /yacd

RUN npm -g install pnpm
RUN pnpm install && pnpm build

FROM rust as backend
RUN git clone https://github.com/Watfaq/clash-rs.git
WORKDIR /clash-rs

RUN cargo build --release --jobs=$(nproc)

FROM ubuntu

COPY --from=frontend /yacd/public /ui
COPY --from=backend /clash-rs/target/release/clash /usr/local/bin/

ENTRYPOINT ["clash"]
