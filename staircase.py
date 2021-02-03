#hackerrank problem 
#staircase
n = int(input(''))
i1 = n-1
i2 = 1
for i in range (n):
	print(' '*i1+'#'*i2)
	i1-=1
	i2+=1