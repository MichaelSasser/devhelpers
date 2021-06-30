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

from _pytest.capture import CaptureFixture

from devhelpers.timeit import timeit


@timeit(100)
def setup_100(a: int, b: int) -> int:
    c: int = 0
    for _ in range(10):
        c = a + b + c
    return c


@timeit
def setup_1(a: int, b: int) -> int:
    c: int = 0
    for _ in range(10):
        c = a + b + c
    return c


def test_timeit_no_interfearence_100() -> None:
    # Setup
    desired: int = 30

    # Exercise
    actual: int = setup_100(1, 2)  # type: ignore

    # Verify
    assert actual == desired

    # Cleanup - None


def test_timeit_no_interfearence_1() -> None:
    # Setup
    desired: int = 30

    # Exercise
    actual: int = setup_1(1, 2)

    # Verify
    assert actual == desired

    # Cleanup - None


def test_timeit_has_output_100(capsys: CaptureFixture) -> None:
    # Setup
    # desired = "TimeIt: setup_1(args=(1, 2), kwargs={}) took"
    desired: str = (
        "TimeIt: setup_100(args=(1, 2), kwargs={}) ran 100 times "
        "and took: total ="
    )
    setup_100(1, 2)  # type: ignore

    # Exercise

    captured = capsys.readouterr()
    actual: str = captured.out

    # Verify
    assert actual.startswith(desired)

    # Cleanup - None


def test_timeit_has_output_1(capsys: CaptureFixture) -> None:
    # Setup
    desired: str = "TimeIt: setup_1(args=(1, 2), kwargs={}) took"

    setup_1(1, 2)

    # Exercise

    captured = capsys.readouterr()
    actual: str = captured.out

    # Verify
    assert actual.startswith(desired)

    # Cleanup - None
