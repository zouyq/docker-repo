# tailscale derper deploy on fly.io
FROM golang:alpine AS builder

RUN apk add git

RUN git clone https://github.com/tailscale/tailscale.git
WORKDIR tailscale

RUN sed -i '/ss.ListenAndServe(net.JoinHostPort(/s/listenHost/"fly-global-services"/' cmd/derper/derper.go

RUN go build -o derper -a ./cmd/derper

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /go/tailscale/derper /usr/local/bin

ENTRYPOINT ["derper"]