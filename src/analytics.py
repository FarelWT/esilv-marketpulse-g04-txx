
def index_by_date(prices):
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    instrument = index_by_date(instrument_prices)
    benchmark = index_by_date(benchmark_prices)

    common_dates = sorted(set(instrument) & set(benchmark))

    return (
        [instrument[date] for date in common_dates],
        [benchmark[date] for date in common_dates]
    )


def calculate_period_return(prices):
    return (prices[-1]["close"] / prices[0]["close"] - 1) * 100


def calculate_relative_performance(instrument_return, benchmark_return):
    return instrument_return - benchmark_return


def calculate_base_100(prices):
    first_close = prices[0]["close"]

    return [
        {
            "date": row["date"],
            "ticker": row["ticker"],
            "value": row["close"] / first_close * 100
        }
        for row in prices
    ]
