FROM alpine AS builder

RUN apk add build-base autoconf automake libtool git

RUN git clone https://github.com/troglobit/libuev.git /libuev
WORKDIR /libuev
RUN ./autogen.sh && ./configure && make && make install-strip

RUN  git clone https://github.com/troglobit/uredir.git /uredir

WORKDIR /uredir

RUN ./autogen.sh && ./configure
RUN make -j$(nproc)

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /uredir/uredir /usr/local/bin/

ENTRYPOINT ["uredir"]