# Fibonacci
Different ways of calculating fibonacci in Python

The first function, slow_fib, uses recursion to calculate the nth number of a fibonacci sequence but does so very inefficiently.
The reason for this inefficiency is that each call to slow_fib makes recursive calls to slow_fib for n-2 and n-1. So if we start
with slow_fib(100), we call slow_fib(98) and slow_fib(99) recursively but each of these calls must also call slow_fib for n-2 and
n-1 so we end up having 2^n calls to fib(n). For any n over 30, the amount of calls to slow_fib would be somewhere in the billions,
which would take a very long time to calculate. For example, slow_fib(30) takes .7 seconds on my system, while slow_fib(35) takes
7.4 seconds. Even the next number in the fibonacci sequence, 36, takes 16.8 seconds to calculate, so we can see the time it takes to
calculate all those additions is not linear, but rather exponential (2^n). 

The next function, fib_sum, uses iteration with a for loop to sum up two numbers at a time to generate the fibonacci sequence, starting 
with the base case 0 and 1. There is no inefficiency here, addition is performed very quickly and we only need one iteration per each 
number in the fibonacci sequence. Even a call for fib_sum(10000) only takes .1 seconds. 

We use the same idea but with recursion for fast_fib. Using a helper function is necessary because calls to fast_fib only have knowledge
of n, whereas we need the ability to remember n and two sequential numbers of the fibonacci sequence. The recursive calls perform the 
same function as iteration in the previous function, fib_sum. If there are more numbers in the fibonacci sequence to calculate (n is not
zero) then we simply call fib_helper with the values b for a and a+b for b. Finally when we've finished these recursive calls and additions
n is equal to zero and we return a, the nth fibonacci number.
