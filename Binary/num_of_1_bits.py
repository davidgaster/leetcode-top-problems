class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Answer is the number of remainders equal to 1 (odd set bits), as
        you divide n by 2 until it reaches 0.
        '''
        count = 0
        while n > 0:
            count += n % 2
            n //= 2
        return count