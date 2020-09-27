FROM marhoy/balena-wpe

RUN install_packages curl

COPY udev-rules/ /etc/udev/rules.d/

COPY wpe-init /wpe-init
RUN chmod +x /wpe-init

COPY hyperpixel4-init /hyperpixel4-init
RUN chmod +x /hyperpixel4-init

COPY public_html /var/lib/public_html

CMD [ "/wpe-init" ]

ENV TOHORA_VERSION=0.3.2
RUN wget -O tohora.tgz \
    "https://github.com/mozz100/tohora/releases/download/v"$TOHORA_VERSION"/tohora_"$TOHORA_VERSION"_Linux_armv5.tar.gz" \
    && tar xzf tohora.tgz \
    && rm tohora.tgz
