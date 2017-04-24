# Countdown Numbers Round
# 21 August 2016
# Jason White

# countdown2
# 22 April 2017
# 1. Put functions in
# 2. Changed some variable names
# 3. Remove divisions that do not produce an integer result
# 4. Added a single level of parenthesis around x + y and x - y


import itertools
import random

def select_numbers():
    # Return a list of numbers to choose from
    high = list(range(25, 125, 25))
    low  = list(range(1, 11)) * 2
    random.shuffle(high)
    random.shuffle(low)
    num_high = random.randint(0, 4)
    num_low  = 6 - num_high
    return high[0:num_high] + low[0:num_low]

def number_permutations(in_numbers):
    # create a list of all possible permutations
    perms = []
    for i in range(2, len(in_numbers) + 1):
        perms += list(itertools.permutations(in_numbers, i))
    return perms
    
def operator_combinations(in_nums):
    # Return all the combinations of operators
    length = len(in_nums) - 1
    ops = ["+", "-", "*", "/"]
    sums = ops
    if length > 1:
        for k in range(length - 1):
            tmp = []
            for i in sums:
                for j in range(4):
                    tmp.append(i + ops[j])
            sums = tmp
    return sums

def create_sums(number_perms):
    sums = []
    for i in number_perms:
        for j in operator_combinations(i):
            tmp = [i[0]]
            for k in range(len(j)):
                tmp.append(j[k])
                tmp.append(i[k + 1])
            sums.append(tmp)
    return sums

# computer chooses numbers to use to reach target

selected_numbers = select_numbers()

print("Selected numbers : ", selected_numbers)

# computer chooses target number
target = random.randint(100, 999)
print("Target number    : ", target)

number_perms = number_permutations(selected_numbers)

sums = create_sums(number_perms)

print(random.choice(sums))

# check sums for solution

found = False
for sum in sums:
    if target == eval(sum):
        print("Solution         : ", sum, "=", eval(sum))
        found = True
        break
if not found:
    print("Solution         :  Not found")
