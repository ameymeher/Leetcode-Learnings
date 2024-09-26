class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        incoming = defaultdict(set)
        outgoing = defaultdict(set)
        can_take = set([i for i in range(numCourses)])

        for c,pre in prerequisites:
            incoming[c].add(pre)
            outgoing[pre].add(c)
            if c in can_take:
                can_take.remove(c)

        can_take = list(can_take)

        ans = []

        for c in can_take:
            ans.append(c)

            #Remove the incomings from the outgoings of c
            for out in outgoing[c]:
                incoming[out].remove(c)
                if not incoming[out]:
                    can_take.append(out)
                    del incoming[out]

        if len(ans) != numCourses:
            return []

        return ans