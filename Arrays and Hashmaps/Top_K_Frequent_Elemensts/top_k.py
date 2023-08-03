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



# space complexity: O(n) linear time complexity
# time complexity: O(n) linear ... but because of the nested for loop i feel like i'm seeing O(n^2) however because function returns as soon as the length of res reaches k, its not fully looping through the for loop

def topKFrequent2(nums: List[int], k: int) -> List[int]:
    hash = {}
    res = []
    freq = [[] for i in range(len(nums)+ 1)]

    for n in nums:
        hash[n] = 1 + hash.get(n, 0)
    
    for key, val in hash.items():
        freq[val].append(key)
    
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) >= k:
                return res

print(topKFrequent2([1,3,1,3,4,5,2,1], 2))