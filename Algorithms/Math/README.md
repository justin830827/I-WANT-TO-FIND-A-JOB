# Math

This section includes some techniques with mathmetical thinkings. They helps you to find the solution easily.

## Special Algorithms

### Sieve of Eratosthenes (Find Prime)

The Sieve of Eratosthenes is a simple and ingenious[1] ancient algorithm for finding all prime numbers up to any given limit. The main idea here is that every value given to p will be prime, because if it were composite it would be marked as a multiple of some other, smaller prime.

#### Algorithm

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
def isPrime(self, n: int) -> bool:
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
    public boolean isPrime(int n) {
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

### Generate the Next Permutation(Narayana Pandita)

One classic, simple, and flexible algorithm is based upon finding the next permutation in lexicographic ordering, if it exists. It can handle repeated values, for which case it generates each distinct multiset permutation once.
The method goes back to Narayana Pandita in 14th century India, and has been rediscovered frequently. From [Wikipedia](https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order)

#### Algorithm

```
The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.
    1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    2. Find the largest index l greater than k such that a[k] < a[l].
    3. Swap the value of a[k] with that of a[l].
    4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
```

Please check Leecode problem #31 for [Python](./python/next_permutation.py), [Java](./java/NextPermutation.java) implementation.

## Leetcode

|  #   | Title                                                                                                         | Difficulty |                                      Solution                                       | Comments                    |
| :--: | :------------------------------------------------------------------------------------------------------------ | :--------: | :---------------------------------------------------------------------------------: | :-------------------------- |
|  31  | [Next Permutation](https://leetcode.com/problems/next-permutation/)                                           |  `Medium`  |     [Python](./python/next_permutation.py), [Java](./java/NextPermutation.java)     | Narayana Pandita: O(N)      |
| 204  | [Count Primes](https://leetcode.com/problems/count-primes/)                                                   |   `Easy`   |         [Python](./python/count_primes.py), [Java](./java/CountPrimes.java)         | Sieve of Eratosthenes: O(N) |
| 453  | [Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) |   `Easy`   | [Python](./python/min_moves_equal_array.py), [Java](./java/MinMovesEqualArray.java) |                             |
| 1360 | [Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/)           |   `Easy`   |       [Python](./python/number_of_days.py), [Java](./java/NumberOfDays.java)        |                             |
| 1362 | [Closest Divisors](https://leetcode.com/problems/closest-divisors/)                                           |  `Medium`  |     [Python](./python/closest_divisors.py), [Java](./java/ClosestDivisors.java)     |                             |
