# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

 

# Constraints:

#     1 <= s1.length, s2.length <= 104
#     s1 and s2 consist of lowercase English letters.

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create a counter for s1
        s1_counter = Counter(s1)
        s1_len = len(s1)
        
        # Create a sliding window counter for s2
        window_counter = Counter()
        
        for i, char in enumerate(s2):
            # Add the current character to the window
            window_counter[char] += 1
            
            # If the window size is larger than s1, remove the leftmost character
            if i >= s1_len:
                left_char = s2[i - s1_len]
                if window_counter[left_char] == 1:
                    del window_counter[left_char]
                else:
                    window_counter[left_char] -= 1
            
            # Check if the current window is a permutation of s1
            if window_counter == s1_counter:
                return True
        
        return False

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    assert sol.checkInclusion("ab", "eidbaooo") == True, "Test case 1 failed"
    
    # Test case 2
    assert sol.checkInclusion("ab", "eidboaoo") == False, "Test case 2 failed"
    
    # Test case 3
    assert sol.checkInclusion("adc", "dcda") == True, "Test case 3 failed"
    
    # Test case 4
    assert sol.checkInclusion("hello", "ooolleoooleh") == False, "Test case 4 failed"
    
    # Test case 5
    assert sol.checkInclusion("a", "ab") == True, "Test case 5 failed"
    
    print("All test cases passed!")

# Run the test cases
test_solution()
