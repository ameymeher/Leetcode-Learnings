from collections import Counter

def getMinTime(n,requests,minGap):
    counts = Counter(requests)
    counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

    keys = list(counts.keys())

    curr_max_time = counts[keys[0]]*(1+minGap)
    time_remaining = counts[keys[0]]*(minGap)

    for i in range(1,len(keys)):
        if time_remaining - counts[keys[i]] >= 0:
            time_remaining -= counts[keys[i]]
        else:
            counts[keys[i]] -= time_remaining
            curr_max_time += counts[keys[i]]*(1+minGap)
            time_remaining = counts[keys[i]]*(minGap)

    if time_remaining >= minGap:
        return curr_max_time - (minGap)

    return curr_max_time + time_remaining
        

print(getMinTime(12,'abbbacadaeafag',1))