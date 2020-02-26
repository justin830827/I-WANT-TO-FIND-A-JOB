/**
 * Count the number of prime numbers less than a non-negative number, n.
 * 
 * Idea of solution: Use Sieve of Eratosthenes alogorithm
 * 
 * Time Complexity: O(n), Space Complexity: O(n)
 */
public class CountPrimes {
    /**
     * @param n: a non-negative number.
     * @return the number of prime less than n.
     */
    public int countPrimes(int n) {
        // Initialize
        boolean[] isPrime = new boolean[n];
        for (int i = 2; i < isPrime.length; i++) {
            isPrime[i] = true;
        }
        // Loop over to update
        for (int i = 2; i < (int) Math.sqrt(n) + 1; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        // Count number of prime number
        int res = 0;
        for (boolean p : isPrime) {
            if (p)
                res++;
        }
        return res;
    }
}