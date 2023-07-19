
# SOLUTION 1 
# Time complexity: O(n)
# Space complexity: O(n)
def validAnagram(s: str, t: str) -> bool:
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

print(validAnagram(s, t))
    