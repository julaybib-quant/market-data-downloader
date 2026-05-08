from typing import List, Any
from datetime import datetime, timezone


from marketdl.exchanges.base import BaseExchange
from marketdl.exchanges.binance_client import BinanceClient
from marketdl.models.marketdatarequest import MarketDataRequest
from marketdl.models.ohlcv import OHLCV

class BinanceExchange(BaseExchange):
    """
    Binance implementation of BaseExchange.

    Responsibility:
    - Use BinanceClient for API calls
    - Convert raw data into OHLCV domain objects
    """
    def __init__(self, client: BinanceClient) -> None:
        self._client = client
     
    def fetch_ohlcv(self, request: MarketDataRequest) -> List[OHLCV]:

        raw_data = self._client.get_klines(
            symbol=request.symbol,
            interval=request.timeframe,
            limit=500,
        )

        return self._map_to_ohlcv(request, raw_data)
    
    def _map_to_ohlcv(
        self,
        request: MarketDataRequest,
        raw_data: List[List],
    ) -> List[OHLCV]:

        candles: List[OHLCV] = []

        for item in raw_data:

            if len(item) < 6:
                continue

            candles.append(
                OHLCV(
                    symbol=request.symbol,
                    exchange=request.exchange,
                    timeframe=request.timeframe,

                    timestamp=datetime.fromtimestamp(
                        item[0] / 1000, tz=timezone.utc
                    ),

                    open=float(item[1]),
                    high=float(item[2]),
                    low=float(item[3]),
                    close=float(item[4]),
                    volume=float(item[5]),
                )
            )

        return candles