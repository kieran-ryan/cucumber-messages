import math

from .messages import Duration, Timestamp

MILLISECONDS_PER_SECOND = 1e3
NANOSECONDS_PER_MILLISECOND = 1e6
NANOSECONDS_PER_SECOND = 1e9


def milliseconds_since_epoch_to_timestamp(milliseconds_since_epoch: int) -> Timestamp:
    return Timestamp(*to_seconds_and_nanoseconds(milliseconds_since_epoch))


def milliseconds_to_duration(duration_in_milliseconds: int) -> Duration:
    return Duration(*to_seconds_and_nanoseconds(duration_in_milliseconds))


def timestamp_to_milliseconds_since_epoch(timestamp: Timestamp) -> int:
    return to_milliseconds(int(timestamp.seconds), timestamp.nanos)


def duration_to_milliseconds(duration: Duration) -> int:
    return to_milliseconds(int(duration.seconds), duration.nanos)


def add_durations(duration_a: Duration, duration_b: Duration) -> Duration:
    seconds = float(duration_a.seconds) + float(duration_b.seconds)
    nanoseconds = float(duration_a.nanos) + float(duration_b.nanos)
    if nanoseconds >= NANOSECONDS_PER_SECOND:
        seconds += 1
        nanoseconds -= NANOSECONDS_PER_SECOND
    return Duration(int(seconds), int(nanoseconds))


def to_seconds_and_nanoseconds(milliseconds: int) -> int:
    seconds = math.floor(milliseconds / MILLISECONDS_PER_SECOND)
    nanoseconds = math.floor(
        (milliseconds % MILLISECONDS_PER_SECOND) * NANOSECONDS_PER_MILLISECOND
    )
    return seconds, nanoseconds


def to_milliseconds(seconds: int, nanoseconds: int) -> int:
    second_milliseconds = seconds * MILLISECONDS_PER_SECOND
    nano_milliseconds = nanoseconds / NANOSECONDS_PER_MILLISECOND
    return second_milliseconds + nano_milliseconds
