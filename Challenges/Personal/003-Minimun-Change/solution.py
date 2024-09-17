# You are a chashier that only have coins to give as change. You have quarters, dimes, nickels and pennies only.
# Create a function to return the minimun amount of coins to give the exact change, the return must be a list
# following this structure [# of pennies, # of nickels, # of dimes, # quartes]

def make_change(change):
    denominators = [25,10,5,1]
    result = []
    for d in denominators:
        multiplier = change // d
        change -= multiplier * d
        result.append(multiplier)
    result.reverse()
    return result

def assert_change(result, expected):
    assert result == expected, "Incorrect change! Change gave : {} | Should be : {}".format(result, expected)

assert_change(make_change(26), [1,0,0,1])
assert_change(make_change(43), [3,1,1,1])
assert_change(make_change(12), [2,0,1,0])