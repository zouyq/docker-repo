FROM alpine as builder

RUN apk add git build-base

RUN git clone https://github.com/Wind4/vlmcsd.git
WORKDIR vlmcsd

RUN make -j${nproc}

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /vlmcsd/bin/vlmcsd /usr/bin/vlmcsd

ENTRYPOINT ["vlmcsd"]