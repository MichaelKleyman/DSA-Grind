from typing import List

#TIME COMPLEXITY: 0(n log n) + 0(n) + 0(n) + 0(n) for the inner double while loops: final answer is 0(n^2)
# SPACE COMPLEXITY: 0(n^2) due to the main array containing other inner arrays, the loop control variables like i, l, r have and temporary variable sum are constant time complexity
def threeSum(nums: List) -> List:
    res = [] #dominant factor for space complexity

    nums.sort() #sort the entire array, gives a time complexity of 0(n log n)

    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            sum = num + nums[l] + nums[r]

            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([num, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums [l - 1]:
                    l += 1
            
    return res

nums = [-2, 0, 0, 2, 2]
print(threeSum(nums))