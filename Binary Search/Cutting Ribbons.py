class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        def check(val):
            nonlocal ribbons,k
            if val == 0:
                return False
            return sum(list(map(lambda x: x//val,ribbons))) < k

        def bisect_left(arr,val,key):
            l = 0
            r = len(arr)

            while l < r:
                mid = (l+r)//2
                if val <= key(arr[mid]):
                    r = mid
                else:
                    l = mid+1
            return l

        return bisect_left(range(0,max(ribbons)+1),True,check)-1