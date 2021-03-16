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
from itertools import repeat
from sys import float_info
from time import time
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import TypeVar
from typing import Union


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


ReturnType = TypeVar("ReturnType")


def timeit(
    arg: Union[Callable[..., ReturnType], int]
) -> Callable[..., ReturnType]:
    """Use the decorator to time functions in place.

    One hazard: When you use the decorator with a function/method that does
    change something outside it's namespace or a method changes anything
    inside the internal dict, and you let it repeat stuff, might result
    in an unexpected behavior.

    Notes
    -----
    It is safe:

    - when the function/method does not e.g. count, append something
      outside its own namespace, when using the decorator with
      repeating enabled like ``@timeit(100)``.  Or in other words:
      if the internal state does not change, when you call it
      $ n+1 $ times.
    - if you don't repeat anything: ``@timeit``.

    Examples
    --------
    .. code-block:: python

       @timeit(100)
       def foo(a, b):
           pass


       @timeit
       def bar(c, d):
           pass

    :param arg: the callable or number of runs

    """

    def timeit_(func: Callable[..., ReturnType]) -> Callable[..., ReturnType]:
        @wraps(func)
        def wrapper(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
            t_total: float = 0.0
            max_: float = 0.0
            min_: float = float_info.max

            # Runner
            for _ in repeat(None, n):
                t_start: float = time()
                result: Any = func(*args, **kwargs)  # type: ignore
                t_stop: float = time()
                dt: float = t_stop - t_start
                min_ = min(dt, min_)
                max_ = max(dt, max_)
                t_total += dt

            if n > 1:
                print(
                    f"TimeIt: {func.__qualname__}({args=}, {kwargs=}) ran "
                    f"{n} times and took: total = {t_total:4.6E} s, min "
                    f"= {min_:4.6E} s, max = {max_:4.6E} s, avg = "
                    f"{t_total/n:4.6E} s"
                )
            else:
                print(
                    f"TimeIt: {func.__qualname__}({args=}, {kwargs=}) took "
                    f"{t_total:4.6E} s"
                )
            return result

        return wrapper

    # arg can be func, if no n provided. -> @timeit
    # arg can be n, if n provided. -> @timeit(100)
    n = 1
    if isinstance(arg, int):
        n = arg
        return timeit_  # type: ignore
    return timeit_(arg)
