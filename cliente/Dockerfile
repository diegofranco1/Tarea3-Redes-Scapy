DOCKERFILE SCAPY:
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    nano \
    python3 \
    python3-pip \
    texlive-latex-base \
    build-essential \
    libpcap-dev \
    tcpdump \
    iproute2 \
    net-tools \
    iputils-ping \
    git \
    && apt clean

RUN pip3 install --upgrade pip \
    && pip3 install --pre scapy[basic] \
    && pip3 install matplotlib \
    && pip3 install pyx


CMD ["bash"]