FROM alpine:latest as builder

RUN apk add build-base

RUN wget http://ohse.de/uwe/testing/lrzsz-0.12.21rc.tar.gz
RUN tar -xf lrzsz-0.12.21rc.tar.gz
WORKDIR lrzsz-0.12.21rc

RUN sed -i 's/ac_cv_prog_cc_works=no/ac_cv_prog_cc_works=yes/g' configure
RUN ./configure CFLAGS="-std=gnu99 -D_GNU_SOURCE" --disable-nls

RUN sed -i '1i #include <stdlib.h>' lib/long-options.c
RUN find . -name "*.c" -exec sed -i '1i #include <string.h>\n#include <stdio.h>' {} \;
RUN make -j$(nproc) && make install

FROM alpine
LABEL maintainer="zouyq <zyqcn@live.com>"

COPY --from=builder /usr/local/bin /usr/local/bin/

