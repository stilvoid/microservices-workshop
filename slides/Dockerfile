FROM python

RUN DEBIAN_FRONTEND=noninteractive apt-get -q update && apt-get -q -y install graphviz libgif4

RUN curl http://www.princexml.com/download/prince_10r3-1_debian8.0_amd64.deb > prince.deb && dpkg -i prince.deb && rm prince.deb

RUN pip install landslide

COPY ./ /usr/src/app

WORKDIR /usr/src/app

CMD ["/bin/bash", "make.sh"]
