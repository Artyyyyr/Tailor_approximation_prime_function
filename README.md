# Tailor_approximation_prime_function
Program that can draw primery function

start is first value of x
end is last value of x
step is step (that's simple)
y is your function
n is number of chunks that your fubction (y) is divided by
noise is value to reduce rabit jumpes in function

When program reduce jumps, it prints "noise reduced"

It prints two numbers in the end (it is length of function and primery of it, number of points). This numbers should be the same
If they are not, play with parameters: start, end, step, n, noise

When derivitive approaches zero Tailor approximation goes crazy. That's why we use noise parmenr

Also in the end it prints "Integral = " and number. That number is definite integral from paranetr "start" to paranetr "end" of your "y" function
