"""Configure pytest"""

import pytest

EXEC_ARG_NAME = "--stockfish-exec"


def pytest_addoption(parser):
    parser.addoption(
        EXEC_ARG_NAME,
        type=str,
        required=True,
        help="Path to executable stockfish engine",
    )


@pytest.fixture
def stockfish_exec(request):
    return request.config.getoption(EXEC_ARG_NAME)
