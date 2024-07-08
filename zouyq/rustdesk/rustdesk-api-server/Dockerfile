FROM alpine AS builder
LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache git gcc musl-dev mariadb-connector-c-dev pkgconfig

RUN git clone https://github.com/kingmo888/rustdesk-api-server.git

WORKDIR rustdesk-api-server

RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
RUN cp -r db db_bak

ENV HOST="0.0.0.0"

ENTRYPOINT ["sh", "run.sh"]
