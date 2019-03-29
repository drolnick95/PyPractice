# write a method to determine if a string has all unique chars
# O(n) time O(1) space
def is_unique(str):
    seen = set()
    for char in str:
        if char in seen:
            return False
        seen.add(char)
    return True

#implement the above algorithm without using another data structure
# O(n lg n)
def is_unique2(str):
    str = sorted(str)
    if len(str) in [0,1]:
        return True
    for i in range(1, len(str)):
        if str[i-1] == str[i]:
            return False
    return True

