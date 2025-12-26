FROM alpine:latest AS builder

RUN apk add --no-cache \
    build-base \
    git \
    autoconf \
    automake

WORKDIR /build

# 使用维护的 fork
RUN git clone --depth 1 https://github.com/UweOhse/lrzsz.git || \
    git clone --depth 1 https://gitee.com/mirrors/lrzsz.git

WORKDIR /build/lrzsz

# 如果有 autogen.sh
RUN if [ -f autogen.sh ]; then ./autogen.sh; fi

# 配置
RUN ./configure \
    CFLAGS="-std=gnu99 -D_GNU_SOURCE" \
    --prefix=/usr/local \
    --disable-nls

# 编译
RUN make -j$(nproc) && make install

FROM alpine:latest

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /usr/local/bin/* /usr/local/bin/

RUN ln -sf /usr/local/bin/lrz /usr/local/bin/rz && \
    ln -sf /usr/local/bin/lsz /usr/local/bin/sz

CMD ["/bin/sh"]
