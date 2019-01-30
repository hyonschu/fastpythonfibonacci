# fastpythonfibonacci
fastest fibonacci generator in python

uses dual assignments at once to cut out the middleman.

10,000 Fibonacci number in less than 4 ms on 2014 hardware:

```
MacBook Air 1.3GHz (2014)

$ %timeit -n 100 fib(10000)
100 loops, best of 3: 3.79 ms per loop 
```
