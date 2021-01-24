#sum of elements of array
#hackerrank problem
#problem name simple array sum  Practice/Algorithms/Warmup/Simple Array Sum
n = int(input(''))
marks = input('').split(' ') # split function accepts multiple values seperated  by character here is white space
marks_sum = 0
for i in marks:
	marks_sum += int(i) # typecasting value of i to int
print(marks_sum)
