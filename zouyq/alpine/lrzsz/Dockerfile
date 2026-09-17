FROM alpine:latest AS builder

RUN apk add --no-cache build-base

WORKDIR /build

# Upstream git tree is WIP and has no pregenerated configure; use the release tarball.
ADD https://ohse.de/uwe/testing/lrzsz-0.12.21rc.tar.gz /build/lrzsz.tar.gz
RUN tar -xzf lrzsz.tar.gz && mv lrzsz-0.12.21rc lrzsz

WORKDIR /build/lrzsz

# GCC 14+ treats implicit int/function decl as errors; this old C code needs them allowed
RUN CFLAGS="-std=gnu99 -D_GNU_SOURCE -Wno-implicit-int -Wno-implicit-function-declaration -Wno-error" ./configure \
    --prefix=/usr/local \
    --disable-nls

RUN make -j$(nproc) && make install

FROM alpine:latest

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /usr/local/bin/* /usr/local/bin/

RUN ln -sf /usr/local/bin/lrz /usr/local/bin/rz && \
    ln -sf /usr/local/bin/lsz /usr/local/bin/sz

CMD ["/bin/sh"]
