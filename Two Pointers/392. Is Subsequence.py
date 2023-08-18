class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 1:
            return s[0] in t
        if len(s) == 0 or (len(s) == 0 and len(t) == 0):
            return True
        first = left = 0
        last = len(s) - 1
        right = len(t) - 1
        while left < right:
            if t[left] == s[first]:
                first += 1
            left += 1
            if t[right] == s[last]:
                last -= 1
            right -= 1
            if first > last:
                break
        else:
            return False
        return True
