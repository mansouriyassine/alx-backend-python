#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code
and apply any necessary changes.
"""

from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Zoom in on each element of the input tuple by
    repeating it 'factor' times.

    Args:
        lst (Tuple[Any, ...]): The input tuple.
        factor (int): The factor by which to zoom in. Default is 2.

    Returns:
        List[Any]: The zoomed-in list.
    """
    zoomed_in: List[Any] = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[Any, ...] = (12, 72, 91)

zoom_2x: List[Any] = zoom_array(array)

zoom_3x: List[Any] = zoom_array(array, 3)