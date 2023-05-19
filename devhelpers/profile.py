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
from functools import wraps
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import TypeVar
from cProfile import Profile
from io import StringIO
from pstats import Stats
from pstats import SortKey


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


ReturnType = TypeVar("ReturnType")


def profile(func: Callable[..., ReturnType]) -> Callable[..., ReturnType]:
    """Profile a function.

    https://docs.python.org/3/library/profile.html#profile.Profile

    Examples
    --------
    .. code-block:: python

       @profile
       def foo(a, b):
           pass

    :param func: a function

    """

    @wraps(func)
    def wrapper(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
        pr: Profile = Profile()
        pr.enable()
        result: Any = func(*args, **kwargs)
        pr.disable()
        stream: StringIO = StringIO()
        stats: Stats = Stats(pr, stream=stream).sort_stats(SortKey.CUMULATIVE)
        stats.print_stats()
        print(stream.getvalue())
        return result

    return wrapper


# vim: set ft=python :
