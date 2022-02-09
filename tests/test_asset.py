import pytest
from perfcalc.asset import Asset


@pytest.fixture(name='new_asset')
def fixture_new_asset():
    new_asset = Asset()
    yield new_asset


def test_create_asset(new_asset):
    assert new_asset
