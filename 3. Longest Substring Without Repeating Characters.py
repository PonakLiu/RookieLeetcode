class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = len(s)
        if (lens == 0):
            return 0
        map = {}
        first = 0
        second = 0
        map[s[0]] = 0
        max_val = 1
        while (second < lens - 1):
            second += 1
            if (s[second] in map and map[s[second]] >= first):
                first = map[s[second]] + 1
            map[s[second]] = second
            max_val = max([max_val, second - first + 1])
            print("first: {} second: {} max_val: {}".format(first, second, max_val))
        return max_val


s = Solution()
a = "abba"
print(s.lengthOfLongestSubstring(a))
