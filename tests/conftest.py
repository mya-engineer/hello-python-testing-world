import pytest
import sys


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {
        'stdout': '',
        'write_calls': 0
    }

    def fake_write(output):
        buffer['stdout'] += output
        buffer['write_calls'] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture(scope='session')  # caches connection and passes to fixtures
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connect drops after test with yield
        yield conn
