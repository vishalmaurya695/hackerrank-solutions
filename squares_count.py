#count the no of perfect squares in given range
#hackerrank problem
import math
num_list = []
start = int(input('start value'))
end = int(input('end value'))
perfect_squares = []
num_list.extend(range(start,end))
print(num_list)

for i in num_list:
	root = math.sqrt(i)
	floor = math.floor(root)
	if floor * floor == i:
		perfect_squares.append(i)


print('perfect squares',perfect_squares)