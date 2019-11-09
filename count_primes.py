# Count the number of prime numbers less than a non-negative number, n.

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        for i in range(2, n+1):
            isPrime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    isPrime = False
                    break
                    
            if isPrime:
                result.append(i)
        
        return len(result)