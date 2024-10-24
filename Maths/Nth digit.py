class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        1-9 9 digits
        10-99 90*2 digits
        100-999 900*3 digits
        1000-9999 9000*4 digits
        """

        ran = 9
        length = 1

        while n > ran*length:
            n -= ran*length
            ran*=10
            length+=1
        
        n-=1
        base = pow(10,length-1)
        q,r = divmod(n,length)
        return int(str(base+q)[r])