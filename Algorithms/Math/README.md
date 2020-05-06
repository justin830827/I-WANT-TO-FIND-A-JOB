# Math

This section includes some techniques with mathmetical thinkings. They helps you to find the solution easily.

## Special Algorithms

### Sieve of Eratosthenes

The Sieve of Eratosthenes is a simple and ingenious[1] ancient algorithm for finding all prime numbers up to any given limit. The main idea here is that every value given to p will be prime, because if it were composite it would be marked as a multiple of some other, smaller prime.

#### Pseudocode

```
Algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.

    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n do
                A[j] := false

    return all i such that A[i] is true.
```

#### Python

```python
def isPrimes(self, n: int) -> bool:
    if n < 2: return False # False is Input less than 2
    # Declare array to record if value if prime
    is_prime = [False if i < 2 else True for i in range(n + 1)]

    # Loop over to update the array
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime[-1]
```

#### Java

```java
class Prime {
    public boolean IsPrime(int n) {
        // Initialize
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i < isPrime.length; i++) {
            isPrime[i] = true;
        }
        // Loop over to update
        for (int i = 2; i < (int)Math.sqrt(n + 1) + 1; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n + 1; j+=i) {
                    isPrime[j] = false;
                }
            }
        }
        return n < 2 ? false : isPrime[n];
    }
}

```

## Leetcode

|  #   | Problem                                                                                                       | Difficulty |                                      Solution                                       | Follow-up |
| :--: | :------------------------------------------------------------------------------------------------------------ | :--------: | :---------------------------------------------------------------------------------: | :-------- |
| 453  | [Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) |   `Easy`   | [Python](./python/min_moves_equal_array.py), [Java](./java/MinMovesEqualArray.java) | 462,      |
| 1360 | [Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/)           |   `Easy`   |       [Python](./python/number_of_days.py), [Java](./java/NumberOfDays.java)        |           |
| 1362 | [Closest Divisors](https://leetcode.com/problems/closest-divisors/)                                           |  `Medium`  |     [Python](./python/closest_divisors.py), [Java](./java/ClosestDivisors.java)     |           |
| 204  | [Count Primes](https://leetcode.com/problems/count-primes/)                                                   |   `Easy`   |         [Python](./python/count_primes.py), [Java](./java/CountPrimes.java)         |           |
