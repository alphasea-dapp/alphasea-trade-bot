from unittest import TestCase
from unittest.mock import MagicMock
from src.utils import fetch_tickers, create_ccxt_client
import pandas as pd
from pandas.testing import assert_frame_equal

# https://github.com/ccxt/ccxt/wiki/Manual#ticker-structure


class TestUtilsFetchTickers(TestCase):
    def test_ok_ftx(self):
        client = create_ccxt_client('ftx')

        df = fetch_tickers(client)

        self.assertGreater(df.loc['BTC/USD:USD', 'close'], 10000)
        self.assertEqual(df.index.name, 'symbol')
        self.assertEqual(df.columns, ['close'])

    def test_ok_binance(self):
        client = create_ccxt_client('binance')

        df = fetch_tickers(client)
        print(df)

        self.assertGreater(df.loc['BTC/USDT', 'close'], 10000)
        self.assertEqual(df.index.name, 'symbol')
        self.assertEqual(df.columns, ['close'])
