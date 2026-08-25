"""Tests for the pure helpers in scripts/standard_stats.py."""

from datetime import datetime

import standard_stats as ss


def test_twelve_months_ago_basic():
    assert ss._twelve_months_ago(datetime(2026, 8, 25)) == (2025, 8)


def test_twelve_months_ago_january_wraps_year():
    assert ss._twelve_months_ago(datetime(2026, 1, 15)) == (2025, 1)
    assert ss._twelve_months_ago(datetime(2026, 12, 1)) == (2025, 12)


def test_date_in_window_boundaries():
    # [lo, end) — inclusive lower, exclusive upper
    assert ss._date_in("2025-08", (2025, 8), (9999, 1))
    assert not ss._date_in("2025-07", (2025, 8), (9999, 1))
    assert ss._date_in("9999-01", (2025, 8), (9999, 1)) is False, "exclusive upper bound"


def test_date_in_prior_window():
    cur = (2025, 8)
    prev = (2024, 8)
    assert ss._date_in("2024-08", prev, cur)
    assert ss._date_in("2025-07", prev, cur)
    assert not ss._date_in("2024-07", prev, cur)
    assert not ss._date_in("2025-08", prev, cur)


def test_date_in_malformed():
    assert ss._date_in("", (2025, 8), (9999, 1)) is False
    assert ss._date_in("notadate", (2025, 8), (9999, 1)) is False
    assert ss._date_in(None, (2025, 8), (9999, 1)) is False
