"""
Assumptions:
1. First word is the name. Can it be ""? Assuming it won't be
2. Duplicate names can exist, but they might be different
3. If a email is same, then we have to group them and I'm assuming the name for both would be the same
4. Return a list of merged accounts
5. There should be atleast one email for the name

[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

John: [set1, set2, set3]

{
    "John" : [set("johnsmith@mail.com","john00@mail.com","john00@mail.com"),set("johnnybravo@mail.com")]
    "Mary" : [set("mary@mail.com")]
}
common = [0]
new_emails = set("johnsmith@mail.com","john00@mail.com","john00@mail.com")

1. I became too quiet as the time was going. Though I was able to solve this question with just one change from append to extend
2. When defining class functions, use self in the signature of the functions
3. + concatenates two lists

"""

# My first solution, not that efficient
from collections import defaultdict
acc_map = defaultdict(list)

def merge_accounts(accounts):
    for account in accounts:
        name = account[0]

        if name not in acc_map:
            acc_map[name].append(set(account[1:]))
        else:
            common = []
            new_emails = set(account[1:])
            for i,acc_set in enumerate(acc_map[name]):
                if len(new_emails & acc_set) > 0:
                    common.append(i)
            
            for i in common:
                new_emails.update(acc_map[name][i])
            
            for i in reversed(common):
                acc_map[name].pop(i)

            acc_map[name].append(new_emails)

    res = []
    for name, email_arr in acc_map.items():
        for email_set in email_arr:
            acc = []
            acc.append(name)
            acc.extend(sorted(email_set))
            res.append(acc)

    return res



class UnionFind:

    #O(N) space for storing parents
    def __init__(self,n):
        self.p = [i for i in range(n)]
        self.r = [0]*n

    #O(N) time for finding the parent in the worst case, used path compression so won't be that
    # Can consider O(1)
    def find(x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    # O(N) time for doing the union
    # Can consider O(1)
    def union(x,y):
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

def merge_accounts(arr):
    
    dsu = UnionFind(len(arr))

    email_map = {}

    for i,account in enumerate(arr):
        for email in account[1:]:
            if email in email_map and i != email_map[email]:
                email_map[email] = dsu.union(email_map[email],i)
            else:
                email_map[email] = i

    acc_map = defaultdict(list)

    for email, i in email_map.items():
        acc_map[dsu.find(i)].append(email)

    res = []
    for i, email_arr in acc_map.items():
        res.append([arr[i][0]] + sorted(email_arr))

    return res

"""
[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]


dsu
p [0, 0, 2, 3]


email_map {
    johnsmith@mail.com : 0,
    john_newyork@mail.com: 0,
    john00@mail.com: 1,
    mary@mail.com:2,
    johnnybravo@mail.com:3
}

acc_map {
    0: [johnsmith@mail.com,john_newyork@mail.com,john00@mail.com],
    2: [ mary@mail.com],
    3: [johnnybravo@mail.com]
}

res = [["John",john00@mail.com,john_newyork@mail.com,johnsmith@mail.com],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

"""