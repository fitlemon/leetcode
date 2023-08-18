class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        count_of_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                count_of_vowels += 1
        global_max = count_of_vowels
        for i in range(len(s) - k):
            count_of_vowels += (s[i + k] in vowels) - (s[i] in vowels)
            global_max = max(global_max, count_of_vowels)

        return global_max


s = "abciiidef"
k = 3
foo = Solution()
bar = foo.maxVowels(s, k)
print(bar)
