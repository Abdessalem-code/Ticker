from dataclasses import dataclass
from datetime import datetime

@dataclass
class Stock:
    _symbol: str
    _date: datetime
    _open: float
    _high: float
    _low: float
    _close: float
    _volume: int
    _openInt: int

    def update(self, 
               Date: datetime,
               Open: float,
               High: float,
               Low: float,
               Close: float,
               Volume: int,
               OpenInt: int):
        self._date = Date
        self._open = Open
        self._high = High
        self._low = Low
        self._close = Close
        self._volume = Volume
        self._openInt = OpenInt

    @property
    def symbol(self):
        return self._symbol

    @property
    def date(self):
        return self._date

    @property
    def open(self):
        return self._open

    @property
    def high(self):
        return self._high

    @property
    def low(self):
        return self._low

    @property
    def close(self):
        return self._close

    @property
    def volume(self):
        return self._volume

    @property
    def openInt(self):
        return self._openInt
