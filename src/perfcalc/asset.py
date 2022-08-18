"""Module defines asset characteristics."""


# pylint: disable=R0903
class Asset:
    """Class defines asset characteristics."""

    def __init__(self, default_lang, ccy, ext_id, fund_dict):
        """Define asset class attributes."""
        self._set_currency(ccy)
        self._set_external_id(ext_id)
        self._set_default_lang(default_lang)
        self._set_fund_dict(fund_dict)

    def _set_external_id(self, ext_id):
        """Set external identifier."""
        self.ext_id = ext_id

    def _set_fund_dict(self, fund_dict):
        """Set dictionary of fund names.

        Raises ValueError if default fund language is in defined fund name
        languages.
        """
        fund_languages = fund_dict.keys()
        if self.default_lang not in fund_languages:
            raise ValueError(
                f"Defined fund languages: {fund_languages} do not match\
                default language: {self.default_lang}"
            )
        self.fund_dict = fund_dict

    def _set_currency(self, ccy):
        """Set currency."""
        self.ccy = ccy

    def _set_default_lang(self, default_lang):
        """Set default fund name language."""
        self.default_lang = default_lang

    def __str__(self):
        """Display asset characteristics."""
        return f"{self.ccy}"
