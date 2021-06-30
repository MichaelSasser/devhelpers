#!/usr/bin/env python
# devhelpers - A Development Toolbox
# Copyright (c) 2021  Michael Sasser <Michael@MichaelSasser.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import annotations

import pytest

from devhelpers.isatomic import NotAtomicError
from devhelpers.isatomic import isatomic


tests: int = 0  # store the number of tests


@isatomic(100)
def setup_100(a: int, b: int) -> int:
    global tests
    tests += 1
    if tests == 99:
        return -1
    return a + b


@isatomic
def setup_2(a: int, b: int) -> int:
    return a + b


@isatomic
def setup_2_fail() -> int:
    global tests
    tests += 1
    return tests


def test_isatomic_100_fail_99() -> None:
    # Setup
    desired: str = (
        "The function is not atomic! This was confirmed during iteration 99. "
        'The return value of the first iteratrion was "49". The result of '
        'iteration 99 is "-1".'
    )
    actual: str = "ChangedLater"

    # Exercise
    with pytest.raises(NotAtomicError) as excinfo:
        setup_100(7, 42)  # type: ignore
    actual = str(excinfo.value)

    # Verify
    assert actual == desired

    # Cleanup
    global tests
    tests = 0


def test_isatomic_2() -> None:
    # Setup
    desired: int = 49

    # Exercise
    actual: int = setup_2(7, 42)

    # Verify
    assert actual == desired

    # Cleanup - None


def test_isatomic_2_fail() -> None:
    desired: str = (
        "The function is not atomic! This was confirmed during iteration 2. "
        'The return value of the first iteratrion was "1". The result of '
        'iteration 2 is "2".'
    )
    actual: str = "ChangedLater"

    # Exercise
    with pytest.raises(NotAtomicError) as excinfo:
        setup_2_fail()
    actual = str(excinfo.value)

    # Verify
    assert actual == desired

    # Cleanup
    global tests
    tests = 0
