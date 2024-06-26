FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

ARG STOCKFISH_DIR="stockfish"
ARG STOCKFISH_EXEC="stockfish-ubuntu-x86-64-avx2"
ARG STOCKFISH_ARCHIVE="${STOCKFISH_EXEC}.tar"
ARG GITHUB_URL="https://github.com/official-stockfish/Stockfish"
ARG STOCKFISH_URL="${GITHUB_URL}/releases/latest/download/${STOCKFISH_ARCHIVE}"

RUN apt-get update -y

# Download required tools
RUN apt-get install -y wget

# Install Python
RUN apt-get install -y python3 python3-pip

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

# Download Stockfish
RUN wget $STOCKFISH_URL -O $STOCKFISH_ARCHIVE && \
    tar -xf $STOCKFISH_ARCHIVE && \
    cp "${STOCKFISH_DIR}/${STOCKFISH_EXEC}" $STOCKFISH_EXEC && \
    rm $STOCKFISH_DIR -rdf && \
    rm $STOCKFISH_ARCHIVE

# Clean Docker image
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app