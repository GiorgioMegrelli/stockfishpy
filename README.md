# Stockfishpy

[![PyPI
version](https://badge.fury.io/py/stockfishpy.svg)](https://badge.fury.io/py/stockfishpy)

Python Stockfish UCI Chess Engine wrapper

------------------------------------------------------------------------

## Getting Started:

    pip3 install stockfishpy

-   Python 3.7+
-   [Download](http://www.stockfishchess.com/) and make 'Stockfish'
    executable
-   Setup stockfish PATH in stockfishpy.py

------------------------------------------------------------------------

## USAGE:

Python console Example

``` python
>>> from stockfishpy import *
>>> chess_engine = Engine(STOCKFISH_PATH, param={'Threads': 2, 'Ponder': 'true'})
>>> print(chess_engine.uci())
uciok

>>> print(chess_engine.isready())
readyok

>>> chess_engine.ucinewgame()
>>> chess_engine.setposition('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
>>> move = chess_engine.bestmove()
>>> print(move.bestmove)
e7e5

>>> print(move.ponder)
g1f3

>>> print(move.info)
info depth 12 seldepth 16 multipv 1 score cp -32 nodes 296597 nps 2879582 tbhits 0 time 103 pv e7e5 g1f3 b8c6 f1b5 g8f6 d2d3 f8c5 e1g1 e8g8 b5c6 d7c6 f3e5 d8e7

>>> chess_engine.ucinewgame()
>>> chess_engine.setposition(['e2e4', 'e7e5', 'g1f3'])
>>> move = chess_engine.bestmove()
>>> print(move.bestmove)
b8c6
```

------------------------------------------------------------------------

## Tests:

-   Setup stockfish PATH in stockfishpy.py
-   Execute stockfishtest.py

------------------------------------------------------------------------

## License:

This project is licensed under the GPLv3 see the LICENSE file for
details
