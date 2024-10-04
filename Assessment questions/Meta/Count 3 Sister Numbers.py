def countThreeSisters(l,r):
    count = 0
    for i in range(l,r+1):
        if len(set(list(str(i)))) == 3:
            print(i)
            count+=1
    return count

print(countThreeSisters(876,890)) # 10