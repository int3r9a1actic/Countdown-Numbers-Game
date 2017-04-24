# Countdown Numbers Round
# 21 August 2016
# Jason White

# count
# 21 August 2016
# 1. Lists of numbers to choose from
# 2. Choose numbers
# 3. Generate permutations

# count
# 19 April 2017
# 1. Added combinations of operators
# 2. Added generaion of sums
# 2. Added sums for a solutions

# countdown2
# 22 April 2017
# 1. Put functions in
# 2. Changed some variable names
# 3. Remove divisions that do not produce an integer result
# 4. Added a single level of parenthesis around x + y and x - y


import itertools
import random

def opcombs(in_nums):
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

# create lists of numbers to choose from
numbers_high = list(range(25, 125, 25))
numbers_low  = list(range(1, 11)) * 2
random.shuffle(numbers_high)
random.shuffle(numbers_low)

# computer chooses numbers to use to reach target
selected_high = random.randint(0, 4)
selected_low  = 6 - selected_high

selected_numbers = numbers_high[0:selected_high]
selected_numbers += numbers_low[0:selected_low]

print("Selected numbers : ", selected_numbers)

# computer chooses target number
target = random.randint(100, 999)
print("Target number    : ", target)

# create a list of all possible permutations
permutations = []
for i in range(2, len(selected_numbers) + 1):
    permutations += list(itertools.permutations(selected_numbers, i))

# create sums

sums = []
for i in permutations:
    for j in opcombs(i):
        tmp = str(i[0])
        for k in range(len(j)):
            tmp += j[k]
            tmp += str(i[k + 1])
        sums.append(tmp)

# check sums for solution

found = False
for sum in sums:
    if target == eval(sum):
        print("Solution         : ", sum, "=", int(eval(sum)))
        found = True
        break
if not found:
    print("Solution         :  Not found")
