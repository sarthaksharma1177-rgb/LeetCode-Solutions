# LeetCode Problem 8: String to Integer (atoi) - Medium
# Convert string to integer following atoi rules

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        result = sign * result
        return max(min(result, INT_MAX), INT_MIN)
