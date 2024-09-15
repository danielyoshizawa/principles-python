# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

#     Letter-logs: All words (except the identifier) consist of lowercase English letters.
#     Digit-logs: All words (except the identifier) consist of digits.

# Reorder these logs so that:

#     The letter-logs come before all digit-logs.
#     The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
#     The digit-logs maintain their relative ordering.

# Return the final order of the logs.

 

# Example 1:

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Example 2:

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

 

# Constraints:

#     1 <= logs.length <= 100
#     3 <= logs[i].length <= 100
#     All the tokens of logs[i] are separated by a single space.
#     logs[i] is guaranteed to have an identifier and at least one word after the identifier.

class Node:
    def __init__(self, key:str=None, value:str=None):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def toString(self):
        return self.key + " " + self.value

class Tree:
    def __init__(self):
        self.root = None

    def add(self, key:str, value:str):
        if not self.root:
            self.root = Node(key, value)
        else:
            self._add(key, value, self.root)

    def _add(self, key:str, value:str, node:Node) -> Node:
        if node == None:
            return Node(key, value)

        if value == node.value:
            self._add_balanced((key < node.key), key, value, node)
        else:
            self._add_balanced((value < node.value), key, value, node)
        return node

    def _add_balanced(self, condition:bool, key:str, value:str, node:Node):
        if condition:
            node.left = self._add(key, value, node.left)
        else:
            node.right = self._add(key, value, node.right)
    
    def inorder_travesal(self, root, res):
        if root:
            self.inorder_travesal(root.left, res)
            res.append(root.toString())
            self.inorder_travesal(root.right, res)

def isDigit(word: str) -> bool:
    return word.replace(" ", "").isdigit()

def splitLog(log: str) -> tuple:
    return (log.split(" ", 1))

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digitsList = list()
        tree = Tree()
        for a in logs:
            logSplit = splitLog(a)
            if isDigit(logSplit[1]):
                digitsList.append(a)
            else:
                tree.add(logSplit[0], logSplit[1])

        sorted_arr = []
        tree.inorder_travesal(tree.root, sorted_arr)
        sorted_arr.extend(digitsList)

        return sorted_arr
    
sol = Solution()
assert (sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
assert (sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])
assert (sol.reorderLogFiles(["a1 9 2 3 1","g2 act car", "g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","g2 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])

# Solution 2

class Solution2:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def sorting_algorithm(log):
            # Is a numerical log, make sure these entries appear on the right side without further sorting.
            if log[-1].isnumeric():
                # A tuple of one element. One element tuples need a trailing comma so they are not confused with a simple one (1) or 1 by python.
                return (1,)

            # Is an alphabetical log, use 0 so they are always to the left of the numerical logs, 
            # then use the more complex sorting rules for just the alphabetical logs.
            left_side, right_side = log.split(" ", 1)
            return (0, right_side, left_side)

		# Sort the logs according to the function we defined.
        return sorted(logs, key=sorting_algorithm)
    
sol2 = Solution2()
assert (sol2.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
assert (sol2.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])
assert (sol2.reorderLogFiles(["a1 9 2 3 1","g2 act car", "g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","g2 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])