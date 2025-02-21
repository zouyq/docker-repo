FROM alpine AS builder

RUN apk add build-base autoconf automake libtool git

RUN git clone https://github.com/troglobit/redir.git

WORKDIR redir

RUN ./autogen.sh && ./configure
RUN make -j$(nproc)

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /redir/redir /usr/local/bin/

ENTRYPOINT ["redir"]