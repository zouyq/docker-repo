FROM alpine AS builder

RUN apk add git build-base linux-headers openssl-dev

RUN git clone https://github.com/pymumu/smartdns.git
WORKDIR smartdns

RUN make -j${nproc}

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache libgcc

COPY --from=builder /smartdns/src/smartdns /usr/local/bin/

ENTRYPOINT ["smartdns"]