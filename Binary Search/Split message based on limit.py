"""
Use binary search to search for the answer in a SORTED range.
SORTED is important, always ensure that you are searching in a sorted range.

if parts length is 1, i = 0
    total space = (limit-3-2)*9
if parts length is 2, i = 1
    total space = (limit-3-3)*9 + (limit-3-4)*90
    total space = (limit-3-3)*9 + (limit-3-4)*90
if parts length is 3, i = 2
    total space = (limit-3-4)*9 + (limit-3-5)*90 + (limit-3-6)*900
    total space = (limit-3-4)*9 + (limit-3-5)*90 + (limit-3-6)*900

space = dp[len -1] + (limit-3-(2*len+2))*(parts-pow(10,len-1)+1) - int(''.join('9' for i in range(len-1)))
36 + (9-3-(2*2+2))
"""

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:

        # Max length guess
        max_parts = len(message)

        # Generate the dp
        dp = [0]*(len(str(max_parts))+1)
        diff = ''

        for i in range(len(str(max_parts))):
            dp[i+1] = dp[i] + (limit-3-(2*(i+1)))*9*pow(10,i) - (0 if not diff else int(diff))
            diff+='9'
            if dp[i+1]<=0:
                max_parts = i+1

        # Function to check if the number of parts satisfy the condition or not
        def check(parts):
            nonlocal message

            parts_length = len(str(parts))
            space = (
                        dp[parts_length-1] + 
                        (limit-3-(2*(parts_length)))*(parts-pow(10,(parts_length-1))+1) - 
                        (int(''.join('9' for i in range(parts_length-1))) if parts_length-1 > 0 else 0)
                    )

            return space >= len(message)

        from bisect import bisect_left

        ans = []

        #Answers within range 1-9, 10-99, 100-999, 1000-9999, 10000-99999 likewise are sorted, thus do them differently
        for i in range(1,len(str(len(message)))+1):
            optimal_parts = pow(10,i-1) + bisect_left(range(pow(10,i-1),min(pow(10,i),len(message))),True,key=check)

            if not check(optimal_parts):
                continue
            else:
                cursor = 0
                for i in range(1,optimal_parts+1):
                    suffix = '<' + str(i) + '/' + str(optimal_parts) + '>'
                    ans.append(message[cursor:cursor+limit-len(suffix)] + suffix)
                    cursor+=limit-len(suffix)
                break

        return ans




        