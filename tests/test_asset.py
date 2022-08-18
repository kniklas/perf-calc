"""Module test Asset class."""

import pytest
from perfcalc.asset import Asset

# pylint: disable=C0116 - disable check of docstrings in methods


@pytest.fixture(name="new_asset")
def fixture_new_asset():
    fund_dict = {"EN": "Equity Fund", "PL": "Fundusz Akcji"}
    new_asset = Asset(
        default_lang="PL",
        ccy="USD",
        ext_id="PL123456789012",
        fund_dict=fund_dict,
    )
    yield new_asset


def test_create_asset(new_asset):
    assert new_asset.ccy == "USD"
    assert new_asset.ext_id == "PL123456789012"
    assert new_asset.fund_dict["PL"] == "Fundusz Akcji"
    assert new_asset.default_lang == "PL"


def test_print_asset(new_asset):
    assert new_asset.__str__() == "USD"


def test_wrong_asset_language_name():
    with pytest.raises(ValueError):
        fund_dict = {"EN": "Equity Fund", "PL": "Fundusz Akcji"}
        wrong_asset = Asset(
            default_lang="DE",
            ccy="USD",
            ext_id="PL123456789012",
            fund_dict=fund_dict,
        )
        return wrong_asset
