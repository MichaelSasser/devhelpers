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
from typing import Union


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


ReturnType = TypeVar("ReturnType")


class NotInvariantError(Exception):
    def __init__(self, result_1: Any, result_n: Any, iteration: int):
        msg: str = (
            "The function is not invariant! This was confirmed during "
            f"iteration {iteration}. The return value of the first iteratrion "
            f'was "{result_1}". The result of iteration {iteration} is '
            f'"{result_n}".'
        )
        super().__init__(msg)


def isinvariant(
    arg: Union[Callable[..., ReturnType], int]
) -> Callable[..., ReturnType]:
    """Use the decorator to check if a function is invariant to previous runs.

    The decorator runs a function over and over again and compares the output.
    When the output changes, it raises a `NotInvariantError`.

    Examples
    --------
    .. code-block:: python

       @isinvariant(100)
       def foo(a, b):
           pass


       @isinvariant
       def bar(c, d):
           pass

    :param arg: the callable or number of runs

    """

    def isinvariant_(
        func: Callable[..., ReturnType]
    ) -> Callable[..., ReturnType]:
        @wraps(func)
        def wrapper(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
            result_1: Any = func(*args, **kwargs)

            for i in range(2, n + 1):
                result_n: Any = func(*args, **kwargs)
                if result_n != result_1:
                    raise NotInvariantError(result_1, result_n, i)

            return result_1

        return wrapper

    # arg can be func, if no n provided. -> @isinvariant
    # arg can be n, if n provided. -> @isinvariant(100)
    n = 2
    if isinstance(arg, int):
        n = arg
        return isinvariant_  # type: ignore
    return isinvariant_(arg)


# vim: set ft=python :
