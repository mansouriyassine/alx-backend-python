#!/usr/bin/env python3
"""
Module for type checking functions.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in the given list by repeating each item by a specified factor.
    
    Args:
        lst (Tuple): The input list to be zoomed.
        factor (int, optional): The factor by which each item
        should be repeated. Defaults to 2.
    
    Returns:
        List: The zoomed-in list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array: Tuple[Any, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
