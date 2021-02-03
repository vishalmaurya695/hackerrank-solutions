#compare the triplets
#hackerrank problem


a = input('').split(' ')
b = input('').split(' ')

alice = 0
bob = 0
for i in range(3):
	if (a[i] != b[i]):
		if int(a[i]) > int(b[i]):
			alice+=1
		elif int(a[i]) < int(b[i]):
			bob+=1
		

print(alice,bob)
