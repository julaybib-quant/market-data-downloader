from typing import Any, List, Dict, Optional
import requests


class BinanceClient:
    """
    Low-level HTTP client for Binance API.

    Responsibility:
    - Handle HTTP requests
    - Manage session
    - Return raw JSON responses
    """

    BASE_URL: str = "https://api.binance.com"

    def __init__(self, timeout: int = 10) -> None:
        self._session: requests.Session = requests.Session()
        self._timeout: int = timeout

    def get_klines(
        self,
        symbol: str,
        interval: str,
        limit: int = 500,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
    ) -> List[List[Any]]:

        endpoint: str = "/api/v3/klines"

        params: Dict[str, Any] = {
            "symbol": symbol.upper(),
            "interval": interval,
            "limit": limit,
        }

        if start_time is not None:
            params["startTime"] = start_time

        if end_time is not None:
            params["endTime"] = end_time

        response = self._session.get(
            url=self.BASE_URL + endpoint,
            params=params,
            timeout=self._timeout,
        )

        response.raise_for_status()
        return response.json()