import pytest
from tokenterminal import TokenTerminal


@pytest.fixture(scope='module')
def token_terminal():
    return TokenTerminal(key='xxxxx-xxxx-xxxx-xxxx-xxxxxxxx')


class TestTokenTerminal:
    def test_get_all_projects(self):
        assert False

    def test_get_historical_metrics(self):
        assert False
