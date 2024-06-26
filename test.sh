#!/bin/bash

STOCKFISH_EXEC=$(find / -type f -name "stockfish-ubuntu-x86-64-*" 2>/dev/null)

if [ -z "${STOCKFISH_EXEC}" ]; then
    echo "Stockfish executable file is not found"
    exit 1
fi

echo "Found: ${STOCKFISH_EXEC}"

python3 -m pytest . --stockfish-exec $STOCKFISH_EXEC
