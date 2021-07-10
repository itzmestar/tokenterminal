import pytest
from tokenterminal import TokenTerminal
import os


@pytest.fixture(scope='module')
def terminal():
    return TokenTerminal(key=os.getenv('API_KEY'))


@pytest.mark.usefixtures('terminal')
class TestTokenTerminal:
    def test_get_all_projects(self, terminal):
        projects = terminal.get_all_projects()
        assert type(projects) is list
        assert len(projects) > 0

    def test_get_historical_metrics(self, terminal):
        project_metrics = terminal.get_historical_metrics('0x')
        assert type(project_metrics) is list
        assert len(project_metrics) > 0
