FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

RUN apk add --no-cache tini busybox-extras

COPY index.html /home
WORKDIR /home

ENTRYPOINT ["tini"]
CMD ["httpd","-f","-v"]