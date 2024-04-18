#!/usr/bin/env python3
from typing import Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zoom in on each element of the input tuple by
    repeating it 'factor' times.

    Args:
        lst (Tuple[int, ...]): The input tuple.
        factor (int): The factor by which to zoom in. Default is 2.

    Returns:
        Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in: Tuple[int, ...] = tuple(
        item
        for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: Tuple[int, ...] = zoom_array(array)

zoom_3x: Tuple[int, ...] = zoom_array(array, 3)