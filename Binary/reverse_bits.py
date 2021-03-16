# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = self.getBits(n)
        bits.reverse()
        ans = self.convert(bits)
        return ans
    
    def getBits(self, n: int) -> int:
        bits = []
        count = 0
        while n > 0:
            b = n%2
            bits.append(b)
            n //= 2
            count += 1
        while count < 32:
            bits.append(0)
            count += 1
        return bits
    
    def convert(self, bits: List[int]) -> int:
        n = 0
        for i,b in enumerate(bits):
            if b==1:
                n += 2**i
        return n