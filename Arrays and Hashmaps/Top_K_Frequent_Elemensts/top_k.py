from typing import List


# space complexity: O(n) Linear time complexity
# time complexity: O(nlogn) Due to the sorting algo using quick sort
def topKFrequent(nums: List[int], k: int) -> List[int]:
    if len(nums) == k:
        return nums
    
    res = []
    hash = {}
    vals = []

    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    
    for key in hash:
        vals.append(hash[key])
    
    vals.sort(reverse=True)

    sorted_vals = vals[:k] #sort up until k, but not including k

    for key,val in hash.items():
        if val in sorted_vals:
            res.append(key)

    return res


print(topKFrequent([1,3,1,3,4,5,2,1], 2))



