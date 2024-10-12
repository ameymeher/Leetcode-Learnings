class UnionFind:

    #O(N) space for storing parents
    def __init__(self,n):
        self.p = [i for i in range(n)]
        self.r = [0]*n

    #O(N) time for finding the parent in the worst case, used path compression so won't be that
    # Can consider O(1)
    def find(self,x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    # O(N) time for doing the union
    # Can consider O(1)
    def union(self,x,y):
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x != p_y:
            if self.r[p_x] > self.r[p_y]:
                self.p[p_y] = p_x
                return p_x

            elif self.r[p_x] < self.r[p_y]:
                self.p[p_x] = p_y
                return p_y

            else:
                self.p[p_y] = p_x
                self.r[p_x]+=1
                return p_x
        return p_x
