#!/usr/bin/env python3
"""
Given the parameters and the return values,
add type annotations to the function.
"""

from typing import Mapping, Any, TypeVar, Union


# Define a generic type variable for the default value
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the
        key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default