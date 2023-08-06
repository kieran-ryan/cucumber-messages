import pathlib
import sys
import time

TESTS_DIR = pathlib.Path(__file__).parent
sys.path.insert(0, str(TESTS_DIR / "../src"))

from cucumber_messages.messages import Duration
from cucumber_messages.time_conversion import (
    add_durations,
    duration_to_milliseconds,
    milliseconds_since_epoch_to_timestamp,
    milliseconds_to_duration,
    timestamp_to_milliseconds_since_epoch,
)


def test_duration_to_milliseconds_string():
    duration = Duration(seconds="3", nanos=40000)

    milliseconds = duration_to_milliseconds(duration)

    assert milliseconds == 3000.04


def test_milliseconds_since_epoch():
    milliseconds_since_epoch = float(time.time()) * 1000
    timestamp = milliseconds_since_epoch_to_timestamp(milliseconds_since_epoch)
    py_epoch_milliseconds_again = timestamp_to_milliseconds_since_epoch(timestamp)

    assert py_epoch_milliseconds_again == milliseconds_since_epoch


def test_duration_to_milliseconds_int():
    duration_in_milliseconds = 1234
    duration = milliseconds_to_duration(duration_in_milliseconds)
    duration_in_milliseconds_again = duration_to_milliseconds(duration)

    assert duration_in_milliseconds_again == duration_in_milliseconds


def test_milliseconds_to_duration_and_back():
    duration_in_milliseconds = 3.000161
    duration = milliseconds_to_duration(duration_in_milliseconds)
    duration_in_milliseconds_again = duration_to_milliseconds(duration)

    assert duration_in_milliseconds == duration_in_milliseconds_again


def test_add_nanos_durations():
    duration_a = milliseconds_to_duration(100)
    duration_b = milliseconds_to_duration(200)

    sum_duration = add_durations(duration_a, duration_b)

    assert sum_duration == Duration(seconds=0, nanos=3e8)


def test_add_seconds_durations():
    duration_a = milliseconds_to_duration(1000)
    duration_b = milliseconds_to_duration(2000)

    sum_duration = add_durations(duration_a, duration_b)

    assert sum_duration == Duration(seconds=3, nanos=0)


def test_add_seconds_and_nanos_durations():
    duration_a = milliseconds_to_duration(1500)
    duration_b = milliseconds_to_duration(1600)

    sum_duration = add_durations(duration_a, duration_b)

    assert sum_duration == Duration(seconds=3, nanos=1e8)


def test_add_seconds_and_nanos_durations_with_legacy_string():
    duration_a = milliseconds_to_duration(1500)
    duration_a.seconds = str(duration_a.seconds)
    duration_b = milliseconds_to_duration(1600)
    duration_b.seconds = str(duration_b.seconds)

    sum_duration = add_durations(duration_a, duration_b)

    assert sum_duration == Duration(seconds=3, nanos=1e8)
