# Copyright (©) 2025, Alexander Suvorov. All rights reserved.
import warnings


def deprecated(new_method_name: str):
    """
    Decorator to mark methods as deprecated.

    Args:
        new_method_name: Name of the replacement method

    Returns:
        function: Decorator function
    """

    def decorator(old_method):
        def wrapper(self, *args, **kwargs):
            warnings.warn(
                f"Method '{old_method.__name__}' is deprecated. Use '{new_method_name}' instead.",
                DeprecationWarning,
                stacklevel=2
            )
            new_method = getattr(self, new_method_name)
            return new_method(*args, **kwargs)

        return wrapper

    return decorator
