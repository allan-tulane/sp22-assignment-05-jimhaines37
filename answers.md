# CMPS 2200 Assignment 5
## Answers

**Name:**_________________________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**

To do this task, we would first select the coin with the largest value that is less than N. To find the largest coin less than N mathematically, we can use: biggestCoin = 2^floor(log_2(N)), because coins are worth 2^k and we use floor to make sure we have an integer and that our coin's value doesnt exceed N. We would then take the the value of this coin and subtract it from N, shown: N - coinVal. We will then repeat the process with this difference as our new N, continuosly decreaseing N until it reaches 0, this way we will have the smallest amount of coins used. We can create a recursive algorithm with this functionality.

In psuedo code:

```
numCoins = 0

foo(N, numCoins)
    if N = 0, return numCoins

    biggestCoin = 2^floor(log_2(N))
    newN = N - biggestCoin
    numCoins += 1

    return foo(newN, numCoins)
```

- **1b.**

Work: W(n) = W(n^logn) + 1

Span: S(N) = S(logn) + 1




- **2a.**

Assume denominations: 1, 6, 8, 10 and assume N = 14

Greedy algorithm will first take 10, because it is the largest value that is less than N. Now, it will take 1 four more times so that N will equal 14 using 5 coins: 10, 1, 1, 1, 1. It cannot take 6 or 8 after 10 because both of these values would cause the total to exceed N.

The actual optimal solution is 2 coins: 6 and 8 so that N = 14. 

Greedy solution will not consider all possible combinations, it will always take the largest value first which may exclude better solutions. We should instead look at all possible solutions first and select the best one. Greedy works well with powers of 2 but not necessarily otherwise.


- **2b.**

If we use dynamic programming to solve this problem, we should find all possible combinations of coins that equal N and then select the solution which requires the least amount of coins. We could store each combination in a tuple that contains a list of coin values and the number of coins used, like: ([10, 1, 1, 1, 1], 5), ([8, 6], 2), and then select the tuple whos second value is the smallest.

W(n) = W(n)

S(n) = S(n)



- **3a.**

Optimal substructure property for MED is:

{MED(S[1:], T[1:]), if S[0] = T[0]
1 + min(MED(S, T[1:]), MED(S[1:], T[1:]), MED(S[1:], T)), otherwise}

where each MED function represents an insertion, a substitution, and a deletion, respectively

