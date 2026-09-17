FROM node:22-alpine AS web-builder

RUN apk add --no-cache git
RUN git clone https://github.com/fatedier/frp.git /frp

# npm workspaces: install from web/ so shared/frpc deps resolve
WORKDIR /frp/web
RUN npm install

WORKDIR /frp/web/frpc
RUN npm run build

FROM golang:1.25-alpine AS go-builder

COPY --from=web-builder /frp /frp
WORKDIR /frp

RUN CGO_ENABLED=0 go build -trimpath -ldflags "-s -w" -tags frpc -o bin/frpc ./cmd/frpc

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache tzdata

COPY --from=go-builder /frp/bin/frpc /usr/local/bin/frpc

ENTRYPOINT ["frpc"]
