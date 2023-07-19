from typing import List


# SOLUTION 1
# Time complexity: O(n)
# Space complexity: O(n)
def twoSum(nums: List[int], target: int) -> List[int]:

    hash = {}

    for i, n in enumerate(nums):
        difference = target - n

        if difference not in hash:
            hash[n] = i
        else:
            return [hash[difference], i]

arr = [3,2,4]
num = 6

# print(twoSum(arr, num))

# SOLUTION 2
# Time complexity: O(n^2)
# Space complexity: O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum(arr, num))