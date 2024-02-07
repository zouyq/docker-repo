FROM alpine as builder

RUN apk add git make curl-dev libc-dev gcc

RUN git clone https://github.com/curl/doh.git
WORKDIR doh

RUN make -j${nproc}

FROM alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache libcurl

COPY --from=builder /doh/doh /usr/local/bin/

ENTRYPOINT ["doh"]