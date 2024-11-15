# Hard 4: Oracle

An oracle is any black-box function where you don't know how the function works on the inside. We have queried this oracle 250 times and placed the results in an array. Each element is the output of the oracle whose input was the index. It looks like: [f(0), f(1), f(2), ...]

We have also found out that the oracle takes on the following structure:

`f(x) = ((x * A) % B * C) % D * E + x % F * G`

This structure has seven prime constants which define it (A,B,C,D,E,F,G). Below are the first 250 outputs of an oracle. What are the seven smallest constants that define this oracle? Format your answer as A:B:C:D:E:F:G

```
[0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204,144,242,182,78,220,116,56,154,94,34,132,72,221,110,259,199,44,237,133,22,171,111,0,149,89,187,127,276,165,61,254,99,39,188,77,17,166,55,204]
```

### Solution

The easiest method is to brute force all $7$ prime numbers by testing every possible combination. However, this $O(n^7)$ function can blow up very fast without some search optimizations. The first thing we notice is that $f$ is cyclic with period of $39$. Since the function $f$ is the sum of two cyclic functions: $f(x)=L(x)+R(x)$, then $39$ must be the least common multiple of the periods of $L$ and $R$. We know all of the constants are prime, so finding the prime decomposition of $39=3\times 13$ means $L$ has period of $3$ and $R$ has period of $13$ or vice versa. This already knocks the complexity down to $O(n^5)$. 

We can also place an upper limit on the multiplier constants because the largest value of $f$ is $276$. The maximum value will occur when the periods are both at their maximum, so $12x+2y=276$, where $x$ and $y$ are the prime multipliers of the $L$ and $R$ functions. The smallest prime is $2$, so if we allow $x=2$ and solve for $y$, we see that the $E$ and $G$ primes must be $E,G\leq113$. 

The problem specifically states that the prime constants need to be the smallest which create this function, which means the order of searching matters. Say we are going to search the first $100$ primes, if we used 5 nested for loops, or a recursion stack with 5 frames, then the code will spend a lot of time searching the higher primes. So we are going to search using a breath-first method instead of depth-first. Start by checking if every constant is the smallest prime, $2$. If not, we are going to introduce the next prime, $3$. Assume the first constant is the new prime and search through all smaller primes for the other constants. Do the same thing for the next constant, until all the constants have been searched using this new prime. If the function still doesn't matter, repeat with the next prime. By continuing this algorithm, it will check all of the smaller prime combinations before moving onto a larger prime. 

A solution employing all of these tactics should run in under a minute.

The constants are `7:13:5:23:11:3:17`.