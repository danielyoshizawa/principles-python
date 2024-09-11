# 859. Buddy Strings

# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

#     For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# Example 1:

# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# Example 2:

# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

# Example 3:

# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

# Constraints:

#     1 <= s.length, goal.length <= 2 * 104
#     s and goal consist of lowercase letters.

def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    if s == goal:
        return len(set(s)) < len(s)  # Check for duplicates

    # Find the indices where the characters differ
    diff = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append((i, s[i], goal[i]))  # Store index and differing characters

    # Check if there are exactly two differences and they can be swapped
    return len(diff) == 2 and diff[0][1] == goal[diff[1][0]] and diff[1][1] == goal[diff[0][0]]

assert buddyStrings("ab", "ba") == True
assert buddyStrings("ab", "ab") == False
assert buddyStrings("aa", "aa") == True
assert buddyStrings("aaaaabc", "aaaaacb") == True