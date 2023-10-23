from argparse import ArgumentParser

from cryptofeed import FeedHandler
from cryptofeed.backends.quest import (
    BookQuest,
    TickerQuest,
    TradeQuest,
)
from cryptofeed.defines import L2_BOOK, TICKER, TRADES
from cryptofeed.exchanges import Coinbase


def parse_args():
    parser = ArgumentParser(
        prog="Crypto Price Streamer",
        description="Application to stream crypto prices to a QuestDB using cryptofeed"
    )
    parser.add_argument("--host", "-H", default="127.0.0.1", type=str, help="QuestDB host fqdn")
    parser.add_argument("--port", "-p", default=9009, type=int, help="ILP Port")
    parser.add_argument("tickers", type=str, nargs="+", help="List of Tickers to scrape")
    parser.add_argument("--currency", "-c", default="USD", help="Currency to express prices in")
    return parser.parse_args()



def main():
    parsed_args = parse_args()
    f = FeedHandler()
    for t in parsed_args.tickers:
        pair = f"{t.upper()}-{parsed_args.currency.upper()}"
        f.add_feed(
            Coinbase(
                channels=[TRADES],
                symbols=[pair],
                callbacks={TRADES: TradeQuest(host=parsed_args.host, port=parsed_args.port)},
            )
        )
        f.add_feed(
            Coinbase(
                channels=[TICKER],
                symbols=[pair],
                callbacks={TICKER: TickerQuest(host=parsed_args.host, port=parsed_args.port)},
            )
        )
    f.run()


if __name__ == "__main__":
    main()
