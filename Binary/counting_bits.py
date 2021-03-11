class Solution:
    def countBits(self, num: int) -> List[int]:
        '''
        Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num, 
        calculate the number of 1's in their binary representation and return them as an array.
        
        Solution: every power of 2 restarts and has the same number of 1's + 1. Ex:
        1: 001
        2: 010
        3: 011
        4: 100
        .
        .
        .
        8: 1000 --> a power of 2 has exactly one 1
        9: 1001 --> # 1 bits resets to 1 + 1 bits starting at 1 and so on
        
        This is the dynamic programming relation:
        numbits[n] = 1 if a power of 2
        numbits[n] = 1 + numbits[current pos] otherwise
        '''
        if num == 0: return [0]
        if num == 1: return [0, 1]
        pows_of_2 = set()
        n = 0
        while 2**n <= num:
            pows_of_2.add(2**n)
            n += 1
        
        ans = [0]*(num+1)
        ans[1] = 1
        dp_idx = 1
        for n in range(2, num+1):
            if n in pows_of_2:
                ans[n] = 1
                dp_idx = 1
            else:
                ans[n] = 1 + ans[dp_idx]
                dp_idx += 1
        
        return ans