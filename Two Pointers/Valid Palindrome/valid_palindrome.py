

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

print(isPalindrome(s))
