from functools import wraps
from typing import Callable, Optional, Awaitable


def acl(allowed_groups=()):
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(request, *args, **kwargs) -> Optional[Awaitable[None]]:
            print('acl decorator for test', allowed_groups)

        return wrapper

    return decorator
