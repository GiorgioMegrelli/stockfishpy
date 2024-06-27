"""Unittests"""

import pytest

from stockfishpy import *


def test_initiate(stockfish_exec):
    with pytest.raises(SystemExit) as _:
        Engine("", param={"Ponder": "false"})


def test_ponder_NoneType(stockfish_exec):
    engine = Engine(stockfish_exec, param={"Ponder": "false"})
    engine.ucinewgame()
    assert engine.bestmove().ponder is None


def test_setdepth(stockfish_exec):
    engine = Engine(stockfish_exec, depth="2")
    engine.ucinewgame()
    assert engine.depth == "2"


def test_check_rightposition(stockfish_exec):
    engine = Engine(stockfish_exec, depth="5")
    allmove = ["e2e4"]
    for x in range(0, 11):
        engine.ucinewgame()
        engine.setposition(allmove)
        allmove.append(engine.bestmove().bestmove)

        # if engine get unrecognized position in loop, it duplicate last bestmove
        assert not (allmove[x] == allmove[x + 1])
