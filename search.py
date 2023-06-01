from typing import Any
import shuffle

def linear_search(collection: list[Any], search: Any) -> bool:
    for idx, item in enumerate(collection):
        if item == search:
            return True

    return False


def binary_search(collection: list[Any], search: Any) -> bool:
    left_idx: int = 0
    right_idx: int = len(collection) - 1

    while left_idx <= right_idx:
        mid_idx: int = (left_idx + right_idx) // 2

        if search == collection[mid_idx]:
            return True
        elif search > collection[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return False


def binary_search_recursive(
    collection: list[Any], search: Any, left_idx: int, right_idx: int
) -> bool:
    if left_idx <= right_idx:
        mid_idx: int = (left_idx + right_idx) // 2

        if search == collection[mid_idx]:
            return True
        elif search > collection[mid_idx]:
            return binary_search_recursive(collection, search, mid_idx + 1, right_idx)
        else:
            return binary_search_recursive(collection, search, left_idx, mid_idx - 1)
    else:
        return False
