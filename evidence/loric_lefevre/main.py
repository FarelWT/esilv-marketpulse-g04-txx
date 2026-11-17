from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

# Ces valeurs correspondent à config/settings.yml.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    """Renvoie le premier cours de clôture."""
    return prices[0]["close"]


def get_last_close(prices):
    """Renvoie le dernier cours de clôture."""
    return prices[-1]["close"]


def display_market_summary(asset, prices, show_currency=True):
    """Affiche un résumé des cours pour un actif."""
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Premier cours de clôture : {first_close}")

    if show_currency:
        print(f"Dernier cours : {last_close} {asset['currency']}")
    else:
        print(f"Dernier niveau : {last_close}")


def main():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===")
    print()

    print("Instrument")
    display_market_summary(instrument, instrument_prices)
    print()

    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)
    print()

    print(f"Period: {LOOKBACK_LABEL}")
    print(f"Interval: {INTERVAL_LABEL}")
    print()

    print("Observations")
    print(f"{instrument['ticker']}: {len(instrument_prices)}")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")


if __name__ == "__main__":
    main()