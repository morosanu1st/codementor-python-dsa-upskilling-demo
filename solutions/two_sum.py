"""Two Sum — hash map pattern (O(n) time, O(n) space)."""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices i, j such that nums[i] + nums[j] == target."""
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], i]
        seen[value] = i
    raise ValueError("no pair found")


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
