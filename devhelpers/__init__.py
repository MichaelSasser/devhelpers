#!/usr/bin/env python
# devhelpers - A Development Toolbox
# Copyright (C) 2021  Michael Sasser <Michael@MichaelSasser.org>
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
# flake8: noqa
# pylint: disable:undefined-variable

"""DevHelpers is a loose collection of python development helpers."""

from __future__ import annotations

from pathlib import Path

from single_source import get_version


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"
__version__: str = (
    get_version(__name__, Path(__file__).parent.parent) or "Unknown"
)

# vim: set ft=python :
