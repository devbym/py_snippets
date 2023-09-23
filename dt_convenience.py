from datetime import date, timedelta, datetime as dt
import time

class xDT(dt):
"""Datetime convenience functions. A weekday starts on monday [0]"""

    _timestamp = time.time()

    timestamp = dt.fromtimestamp(_timestamp)
    now = dt.fromtimestamp(_timestamp).replace(microsecond=0)
    weekday: int = dt.fromtimestamp(_timestamp).utctimetuple().tm_wday
    isoformat = now.isoformat(sep=" ")
    date = now.date()
    time = now.time()

    # weekenddays are [fri] 4, [sat] 5 and [sun] 6
    is_weekend = False
    if 6 - weekday > 0:
        is_weekend = True

    def __repr__(self):
        return f"{self.now}"

    @classmethod
    def calculate(initial,days=0, weeks=0, **kwargs):
        """datetime (dt) supports subtraction of two dt objects returning a timedelta, and addition or subtraction of a dt and a timedelta giving a dt."""
        if days == 0 and weeks == 0:
            return initial.date()
        n = initial.date() + timedelta(days=days, weeks=weeks, **kwargs)
        return n

