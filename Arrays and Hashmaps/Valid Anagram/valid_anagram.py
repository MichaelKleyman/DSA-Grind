
# SOLUTION 1 
# Time complexity: O(n)
# Space complexity: O(n)
from collections import Counter


def validAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_hash, t_hash = {}, {}

    for i in range(len(s)):
        s_hash[s[i]] = 1 + s_hash.get(s[i], 0)
        t_hash[t[i]] = 1 + t_hash.get(t[i], 0)

    for key, val in s_hash.items():
        if key not in t_hash:
            return False
        if t_hash[key] != val:
            return False
    return True

s = 'car'
t = 'acr'

# print(validAnagram1(s, t))
    

# SOLUTION 2 
# Time complexity: O(n log n)
# Space complexity: O(1)
def validAnagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# print(validAnagram2(s, t))


# SOLUTION 3
# Time complexity: O(s+t) --- O(n)
# Space complexity: O(1)
def validAnagram3(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# print(validAnagram3(s, t))

# SOLUTION 4
# Time complexity: 
    # sorting takes O(n log n)
    # and the loop is O(n) because of one for loop
# Space complexity: O(n)
def validAnagram4(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_list, t_list = list(s), list(t)

    s_list.sort()
    t_list.sort()

    for i, n in enumerate(s_list):
        if n != t_list[i]:
            return False
    return True


print(validAnagram4(s, t))


