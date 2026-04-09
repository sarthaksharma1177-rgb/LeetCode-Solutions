# LeetCode Problem 151: Reverse Words in a String - Medium
class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string, filter out empty strings, reverse and join
        return ' '.join(reversed(s.split()))
