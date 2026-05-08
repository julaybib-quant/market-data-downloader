from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MarketDataRequest(BaseModel):
    symbol: str
    exchange: str
    timeframe: str

    # optional boundaries for backfill / partial fetch
    start: Optional[datetime] = Field(default=None)
    end: Optional[datetime] = Field(default=None)