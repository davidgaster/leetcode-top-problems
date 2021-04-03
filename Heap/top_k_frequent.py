# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
class Solution:
    '''
    Approach:
    Count all the numbers using the counter dictionary.
    sort them in ascending order by count (-c)
    take a list of only the values, not the counts and return the top k elements
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_freq = [(-c,num) for num,c in count.items()]
        most_freq.sort()
        ans = [x[1] for x in most_freq]
        return ans[:k]