FROM alpine as builder

RUN apk add git

RUN git clone https://github.com/kingmo888/rustdesk-api-server.git

FROM python:alpine

LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /rustdesk-api-server /rustdesk-api-server
WORKDIR /rustdesk-api-server/

RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
RUN cp -r db db_bak

ENV HOST="0.0.0.0"

ENTRYPOINT ["sh", "run.sh"]
