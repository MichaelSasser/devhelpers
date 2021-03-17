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
import gc

from functools import wraps
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import TypeVar


__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


ReturnType = TypeVar("ReturnType")


def nogc(func: Callable[..., ReturnType]) -> Callable[..., ReturnType]:
    """Use the decorator to disable the garbage collector for a function.

    The garbage collector runs frequently to remove unreachable objects
    from memory. While running the ``@timeit`` decorator, to time functions
    it might be beneficial to disable the garbage collector.

    Notes
    -----
    By disabling the garbage collector, dangling object remain in memory until
    the garbage collector is re-enabled and the garbage is freed.

    If you are sure, you don't have a "leaking" function, this might not be a
    problem. But if the program is "leaky", and you use e.g. the ``timeit``
    decorator, each cycle new objects are created but never freed.

    Make sure you understand the reference counter and the garbage collector
    to not use this decorator for the wrong reasons.

    Examples
    --------
    .. code-block:: python

       @nogc
       @timeit(100)
       def foo(a, b):
           pass


       @nogc
       @timeit
       def bar(c, d):
           pass


       @nogc
       def baz():
           assert not gc.isenabled()

    """

    @wraps(func)
    def wrapper(*args: List[Any], **kwargs: Dict[str, Any]) -> Any:
        gc.disable()
        answer = func(*args, **kwargs)
        gc.enable()
        gc.collect()
        return answer

    return wrapper


# vim: set ft=python :
