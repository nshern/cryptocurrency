import unittest

from converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()
        self.converter.set_price_per_unit("eth", 100)
        self.converter.set_price_per_unit("btc", 2)

    def test_currenct_unknown(self):
        non_existant_currency = "usd"

        with self.assertRaisesRegex(
            ValueError,
            f"The currency you want to convert from, {non_existant_currency}, is unknown",
        ):
            self.converter.convert("usd", "btc", 1)

        with self.assertRaisesRegex(
            ValueError,
            f"The currency you want to convert to, {non_existant_currency}, is unknown",
        ):
            self.converter.convert("btc", "usd", 1)

    def test_logic(self):
        self.assertEqual(
            self.converter.convert(
                from_currency_name="eth", to_currency_name="btc", amount=5
            ),
            250.0,
        )
        self.assertEqual(
            self.converter.convert(
                from_currency_name="btc", to_currency_name="eth", amount=65
            ),
            1.3,
        )
