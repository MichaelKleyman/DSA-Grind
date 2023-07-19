
from typing import List


def contains_duplicates(nums: List[int]) -> bool:
    dict = {}
    for num in nums:
        if num in dict:
            return True
        else:
            dict[num] = 1
    return False

arr = [1,2,3,3,4,1,2]

print(contains_duplicates(arr))
