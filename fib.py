def slow_fib(number):
	# base cases
	if number == 0:
		return 0
	elif number == 1:
		return 1
	# recursively call fib, very inefficient because
	# each recursive call ends up making another
	# recursive call, so we always make 2^n calls
	else:
		return slow_fib(number-2) + slow_fib(number-1)

def fib_sum(number):
	a = 0
	b = 1
	# iteratively sum up the fibonacci numbers
	for i in range(number-2):
		# without using temporary variables
		# set a to b then with the original a,
		# set b to ( a + b ) using python magic
		a, b = b, a + b
	# return the last number of the fibonacci sequence
	return a + b

def fast_fib(n):
	# call fib_helper with the base cases
	return fib_helper(0,1,n)

def fib_helper(a,b,n):
	# when 'iteration' (read recursion) is finished
	# return a to get the answer
	if n == 0:
		return a
	# else call fib_helper with arguments b and sum of a and b
	# essentially 'looping' while calculation the fibonacci sequence
	else:
		return fib_helper(b,(a+b),(n-1))
print(fib_sum(10000))
