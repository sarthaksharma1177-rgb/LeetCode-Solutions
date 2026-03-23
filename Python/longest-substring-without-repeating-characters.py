"""\nLeetCode Problem 3: Longest Substring Without Repeating Characters\nDifficulty: Medium\n\nGiven a string s, find the length of the longest substring without repeating characters.\n\nExample 1:\nInput: s = "abcabcbb"\nOutput: 3\nExplanation: The answer is "abc", with the length of 3.\n"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        Uses sliding window approach with a hashmap.
        
        Time Complexity: O(n)
        Space Complexity: O(min(m, n)) where m is the charset size
        """
        # Dictionary to store the last seen index of each character
        char_index = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            # If character is repeated, move start pointer
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            
            # Update the last seen index of current character
            char_index[s[end]] = end
            
            # Update max length
            max_length = max(max_length, end - start + 1)
        
        return max_length


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3, "Failed: abcabcbb"
    
    # Test case 2
    assert sol.lengthOfLongestSubstring("bbbbb") == 1, "Failed: bbbbb"
    
    # Test case 3
    assert sol.lengthOfLongestSubstring("pwwkew") == 3, "Failed: pwwkew"
    
    # Test case 4
    assert sol.lengthOfLongestSubstring("") == 0, "Failed: empty string"
    
    # Test case 5
    assert sol.lengthOfLongestSubstring("au") == 2, "Failed: au"
    
    print("All test cases passed!")
