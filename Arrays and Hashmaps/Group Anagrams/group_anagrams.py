from typing import List

# SOLUTION 1
# Time Complexity: O(m n log n) -- because of sorting
# Space complexity: O(n)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hashMap = {}
    result = []
    for str in strs:
        # turn the str into a list to begin sorting
        string_list = list(str)
        # sort the list
        string_list.sort()
        # turn it back into a str
        s = ''.join(string_list)

        # check if the sorted string exists in the hash map
        if s in hashMap:
            # if it exists, append it to the existing arr val
            hashMap[s].append(str)
        else:
            # else create a new key val pair
            hashMap[s] = [str]
    
    # now loop through the hash map and append each arr val into the result array
    for key, val in hashMap.items():
        result.append(val)

    return result


arr = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(arr))