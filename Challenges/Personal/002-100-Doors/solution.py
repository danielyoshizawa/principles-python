# You have to pass through 100 doors, all doors are closed in the first pass
# In each pass you will toggle some doors according to the following rules

# In the first pass you will open all the doors
# In the second pass you will toggle only every other door (2nd, 4th, 6th,...)
# In the third pass you will toggle only every third door (3rd, 6th, 9th, ...)
# And so on

# Return a list containing the index of the open doors after the 100th iteration.
# The doors must be numbered from 1 to 100.

# Solution 1 - Brute Force

doors = [False for _ in range(100)]

for i in range(1,101): # O(N^2)
    for j in range(100):
        if (j + 1) % i == 0:
            doors[j] = not doors[j]

result = list()

for k, d in enumerate(doors):
    if d:
        result.append(k+1)

print(result)

# Solution 2 - Optimization

doors = [False for _ in range(101)] # First element will always be false

for i in range(1,101): # O(N)
    for j in range(0,101,i): # Amortization of O(1)
        doors[j] = not doors[j]

result = list()

for k, d in enumerate(doors):
    if d:
        result.append(k)

print(result)

# Solution 3 - Mathematical Approach

# Find the number of divisors of a number, this will be the number of times the door is toggled.
# If it is even, the door is in the same state as the initial one, in our example, closed.
# If it is odd, the door is in the opposite state as the initial one, which is opened.

import math

def number_of_divisors_of(n):
    divisors = set()  # Use a set to avoid duplicates
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)  # Add the corresponding divisor
    return len(divisors)

def is_open_or_closed(n):
    if number_of_divisors_of(n) % 2 == 0:
        return False
    else:
        return True

doors = [is_open_or_closed(n) for n in range(1,101)]

result = list()

for k, d in enumerate(doors):
    if d:
        result.append(k+1)

print(result)

# Solution 4 - Improving the last approach

import math

def is_open(n):
    divisors = set()  # Use a set to avoid duplicates
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)  # Add the corresponding divisor
    return len(divisors) % 2 != 0

print([n for n in range(1,101) if is_open(n)])
