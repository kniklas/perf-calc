"""Module defines asset characteristics."""


# pylint: disable=R0903
class Asset:
    """Class defines asset characteristics."""

    def __init__(self, ccy, ext_id, fname):
        """Define asset class attributes."""
        self.ccy = ccy
        self.ext_id = ext_id
        self.fname = fname
