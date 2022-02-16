"""Module test Asset class."""

import pytest
from perfcalc.asset import Asset

# Disable check of docstrings in methods
# pylint: disable=C0116


@pytest.fixture(name="new_asset")
def fixture_new_asset():
    fund_name = {"EN": "Equity Fund", "PL": "Fundusz Akcji"}
    new_asset = Asset(ccy="USD", ext_id="PL123456789012", fname=fund_name)
    yield new_asset


def test_create_asset(new_asset):
    assert new_asset.ccy == "USD"
    assert new_asset.ext_id == "PL123456789012"
    assert new_asset.fname["PL"] == "Fundusz Akcji"
