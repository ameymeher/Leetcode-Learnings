class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        """
        2,3,5,7,
        2,4,6,10
        """

        primes = []

        def gen_primes():
            valid = [True]*1001
            valid[0] = False
            valid[1] = False

            for i,val in enumerate(valid):
                if val:
                    for j in range(i*i,len(valid),i):
                        valid[j] = False

            return [i for i,val in enumerate(valid) if val]


        primes = gen_primes()

        from bisect import bisect_right

        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= nums[i+1]:
                index = bisect_right(primes,nums[i]-nums[i+1])

                # Always check if the bisect function returns an index which is greater than the list size
                if index >= len(primes):
                    return False

                nums[i]-=primes[index]

                if nums[i] <= 0:
                    return False
        
        return True


"""
[2,3,5,7,11]

"""