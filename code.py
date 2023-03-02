class Solution:
    def majorityElement(self, nums):
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]

        
        
#keep up to two candidates in my counter, so this fulfills the O(N) time and O(1) space requirements.




