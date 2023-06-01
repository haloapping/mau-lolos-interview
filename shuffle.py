import random
from copy import deepcopy
from typing import Any


def knuth_shuffle(collection: list[Any]) -> list[Any]:
    copy_collection = deepcopy(collection)

    for i in range(len(collection) - 1, 0, -1):
        idx_shuffle = len(collection) - i
        idx_unshuffle = random.randint(0, i)

        copy_collection[idx_unshuffle], copy_collection[idx_shuffle] = (
            copy_collection[idx_shuffle],
            copy_collection[idx_unshuffle],
        )

    return copy_collection
