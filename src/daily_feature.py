"""Daily feature: small example module added as a realistic incremental change.
"""

from typing import Iterable, List


def normalize_items(items: Iterable[int]) -> List[int]:
    """Normalize input: coerce to ints and filter None-like values."""
    return [int(x) for x in items if x is not None]


def process_items(items: Iterable[int]) -> List[int]:
    """Simple processing: normalize, filter negatives and square numbers.

    This is a placeholder for a growing feature implemented over multiple commits.
    """
    nums = normalize_items(items)
    return [x * x for x in nums if x >= 0]


def cli_example():
    """Tiny CLI helper used by docs/examples."""
    sample = [1, -2, 3]
    print(process_items(sample))
