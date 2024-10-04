def build_kmp_lookup(pattern):
    lps = [0]*len(pattern)

    prev_lps = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[prev_lps]:
            lps[i] = prev_lps + 1
            i+=1
            prev_lps+=1 
        else:
            if prev_lps == 0:
                lps[i] = 0
                i+=1
            else:
                prev_lps = lps[prev_lps-1]

    return lps

def kmp_search(text,pattern):
    lps = build_kmp_lookup(pattern)

    i=0
    j=0

    count = 0

    while i<len(text):
        if text[i] == pattern[j]:
            i+=1
            j+=1

            if j == len(pattern):
                count+=1
                j = lps[j-1]
        else:
            if j==0:
                i+=1
            else:
                j = lps[j-1]

    return count

def findHowManySubarraysMatchThePattern(numbers,pattern):

    pattern_arr = [0]

    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            pattern_arr.append(1)
        elif numbers[i] < numbers[i-1]:
            pattern_arr.append(-1)
        else:
            pattern_arr.append(0)

    print(f"Pattern array: {pattern_arr}")

    count = 0

    # Brute force
    for i in range(1,len(pattern_arr)-len(pattern)+1):
        for j in range(len(pattern)):
            if pattern_arr[i+j] != pattern[j]:
                break

            if j == len(pattern)-1:
                count+=1

    # Using KMP
    count = kmp_search(pattern_arr,pattern)
    
    return count

print(findHowManySubarraysMatchThePattern([4,1,3,4,4,5,5,6,7,7,8], [1,0,1]))