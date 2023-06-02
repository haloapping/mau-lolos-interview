from typing import Any


def linear_search(collection: list[Any], search: Any) -> tuple[bool, int]:
    for idx, item in enumerate(collection):
        if item == search:
            return True, idx

    return False, -1


def binary_search(collection: list[Any], search: Any) -> tuple[bool, int]:
    left_idx: int = 0
    right_idx: int = len(collection) - 1

    while left_idx <= right_idx:
        mid_idx: int = (left_idx + right_idx) // 2

        if search == collection[mid_idx]:
            return True, mid_idx
        elif search > collection[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return False, -1


def binary_search_recursive(
    collection: list[Any], search: Any, left_idx: int, right_idx: int
) -> tuple[bool, int]:
    if left_idx <= right_idx:
        mid_idx: int = (left_idx + right_idx) // 2

        if search == collection[mid_idx]:
            return True, mid_idx
        elif search > collection[mid_idx]:
            return binary_search_recursive(collection, search, mid_idx + 1, right_idx)
        else:
            return binary_search_recursive(collection, search, left_idx, mid_idx - 1)
    else:
        return False, -1


def min(nums: list[int | float]) -> int | float:
    if len(nums) > 0:
        min: int | float = nums[0]

        for num in nums[1:]:
            if num < min:
                min = num

        return min
    else:
        raise ValueError("nums is empty list")


def max(nums: list[int | float]) -> int | float:
    if len(nums) > 0:
        max: int | float = nums[0]

        for num in nums[1:]:
            if num > max:
                max = num

        return max
    else:
        raise ValueError("nums is empty list")
