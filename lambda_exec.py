# take numbers of list
# [1,2,3], [4,5,6], [7,8,9] ... n
# average of indexed element in list
# i.e. [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3, ...]

# def average(*args):
#   pair_els = zip(*args)
#   total_averages = []
#   for pair in pair_els:
#     total_averages.append(sum(pair)/len(pair))
#   return total_averages

# print(average([1,2,3], [4,5,6], [7,8,9]))

total_averages = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(total_averages([1,2,3], [4,5,6], [7,8,9]))