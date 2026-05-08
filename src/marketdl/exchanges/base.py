from abc import ABC, abstractmethod
from typing import List

from marketdl.models.marketdatarequest import MarketDataRequest
from marketdl.models.ohlcv import OHLCV


class BaseExchange(ABC):
    """
    Abstract contract for all exchanges.

    Every exchange must implement OHLCV retrieval.
    """

    @abstractmethod
    def fetch_ohlcv(self, request: MarketDataRequest) -> List[OHLCV]:
        """
        Fetch OHLCV candles for a given request.
        """
        pass
    