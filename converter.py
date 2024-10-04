class Converter:
    def __init__(self):
        self.prices = {}

    def set_price_per_unit(self, currency_name: str, price: float):
        self.prices[currency_name] = price

    def convert(self, from_currency_name, to_currency_name, amount):
        if (
            from_currency_name not in self.prices
            and to_currency_name not in self.prices
        ):
            raise ValueError(f"{from_currency_name} and {to_currency_name} are unknown")
        elif from_currency_name not in self.prices:
            raise ValueError(
                f"The currency you want to convert from, {from_currency_name}, is unknown"
            )
        elif to_currency_name not in self.prices:
            raise ValueError(
                f"The currency you want to convert to, {to_currency_name}, is unknown"
            )
        else:
            return (
                self.prices[from_currency_name] / self.prices[to_currency_name]
            ) * amount


if __name__ == "__main__":
    c = Converter()
    c.set_price_per_unit("eth", 100)
    c.set_price_per_unit("btc", 2)

    print(c.convert(from_currency_name="eth", to_currency_name="btc", amount=5))
    print(c.convert(from_currency_name="btc", to_currency_name="eth", amount=65))
