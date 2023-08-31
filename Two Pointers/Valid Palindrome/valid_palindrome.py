
# TIME COMPLEXITY: O(n) Linear time complexity : due to two loops happening, but not inner loops
# SPACE COMPLEXITY: 0(n) Linear time complexity: due the new string being made

def isPalindrome(s: str) -> bool:

    if len(s) == 0:
        return True
    
    alnum_str = ''.join(i for i in s if i.isalnum()).lower()

    l = 0
    r = len(alnum_str) - 1

    while l <= r:
        letter1 = alnum_str[l]
        letter2 = alnum_str[r]

        if letter1 != letter2:
            return False

        l += 1
        r -= 1
    
    return True

s = "A man, a plan, a canal: Panama"

# print(isPalindrome(s))


# TIME COMPLEXITY: O(n) Linear time complexity : due to two loops happening, but not inner loops
# SPACE COMPLEXITY: 0(1) Constant time complexity: due no memory being taken up by not making any new strings

def isPalindrome2(s: str) -> bool:
    if len(s) == 0:
        return True

    l, r = 0, len(s) - 1

    while l <= r:

        while l < r and not isAlphaNum(s[l]):
            l += 1

        while r > l and not isAlphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1
    
    return True


def isAlphaNum(c) -> bool:
    return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

print(isPalindrome2(s))