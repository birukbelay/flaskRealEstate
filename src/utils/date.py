from collections import namedtuple
from datetime import datetime, timezone


def utc_now():
    """Current UTC date and time with the microsecond value normalized to zero."""
    return datetime.now(timezone.utc).replace(microsecond=0)

ONE_DAY_IN_SECONDS = 86400
timespan = namedtuple(
    "timespan",
    [
        "days",
        "hours",
        "minutes",
        "seconds",
        "milliseconds",
        "microseconds",
        "total_seconds",
        "total_milliseconds",
        "total_microseconds",
    ],
)

def get_timespan(td):
    """Convert timedelta object to timespan namedtuple."""
    (milliseconds, microseconds) = divmod(td.microseconds, 1000)
    (minutes, seconds) = divmod(td.seconds, 60)
    (hours, minutes) = divmod(minutes, 60)
    total_seconds = td.seconds + (td.days * ONE_DAY_IN_SECONDS)
    return timespan(
        td.days,
        hours,
        minutes,
        seconds,
        milliseconds,
        microseconds,
        total_seconds,
        (total_seconds * 1000 + milliseconds),
        (total_seconds * 1000 * 1000 + milliseconds * 1000 + microseconds),
    )
