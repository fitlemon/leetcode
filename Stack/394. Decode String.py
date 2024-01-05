# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:

# Input: s = "3[a2[c]]a"
# Output: "accaccacc"

# Example 3:

# Input: s = "s2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


class Solution:
    def decodeString(self, s: str) -> str:
        if all(x.isalpha() for x in s):
            return s
        nums = "123456789"
        stack = []
        factor = ""
        while s:
            if s[0].isalpha():
                stack.append(s[0])
            if s[0] in nums:
                factor += s[0]
            if s[0] == "[":
                stack.append(int(factor) * self.decodeString(s[1:]))
            if s[0] == "]":
                factor = ""
            s = s[1:]
            continue
        return "".join(stack)


foo = Solution()
s = "s2[abc]3[cd]ef"
print(foo.decodeString(s))
