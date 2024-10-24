class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []

        def backtrack(curr_i,curr_addr,parts):
            nonlocal s,ans

            if parts < 0:
                return

            if curr_i==len(s):
                if parts == 0:
                    ans.append(curr_addr)
                return

            for i in range(curr_i+1,len(s)+1):
                new_number = s[curr_i:i]

                if ((new_number[0] == '0' and len(new_number) > 1) or
                        int(new_number) > 255):
                    break

                if curr_i == 0:
                    backtrack(i,curr_addr+new_number,parts-1)
                else:
                    backtrack(i,curr_addr + '.' + new_number,parts-1)


        backtrack(0,'',4)

        return ans