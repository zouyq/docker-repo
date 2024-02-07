FROM alpine as builder

RUN apk add git alpine-sdk linux-headers openssl-dev

RUN git clone https://github.com/zerotier/ZeroTierOne.git
WORKDIR ZeroTierOne

RUN make ZT_SSO_SUPPORTED=0 -j${nproc}

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache libstdc++

COPY --from=builder /ZeroTierOne/zerotier-one /usr/local/bin
COPY --from=builder /ZeroTierOne/zerotier-cli /usr/local/bin
COPY --from=builder /ZeroTierOne/zerotier-idtool /usr/local/bin

ENTRYPOINT ["zerotier-one"]