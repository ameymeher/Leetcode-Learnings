"""
Given two strings s1 and s2, find till how many days is s2 a subsequence of s1 if on every day we delete all the strings in s1 from start to end inclusive.

Function Description

Complete the function findDaysS2SubsequenceOfS1 in the editor.

findDaysS2SubsequenceOfS1 has the following parameters:

1. String s1: the original string
2. String s2: the subsequence to find
3. int[] start: the start indices
4. int[] end: the end indices
Returns

int: the number of days s2 is a subsequence of s1

Example 1:

Input:  s1 = "abcdefghabc", s2 = "abc", start = [0, 0, 1, 2, 9], end = [1, 2, 3, 3, 10]
Output: 4 

"""

def findDaysS2SubsequenceOfS1(s1, s2, start, end):
    from collections import defaultdict,deque

    s1_exists = [True] * len(s1)

    indices = defaultdict(deque)

    # Creating the map for the subsequence characters in s1
    for i, char in enumerate(s1):
        if char in set(list(s2)):
            indices[char].append(i)


    def delete_range(start, end):
        
        nonlocal s1, s2, s1_exists, indices

        for i in range(start, end+1):
            
            if s1_exists[i]:
                print(f"Removing {s1[i]}")
                if s1[i] not in set(list(s2)):
                    print("Marking the character deleted which is not in the subsequence")
                    s1_exists[i] = False
                    continue
                
                indices[s1[i]].remove(i)
                if not indices[s1[i]]:
                    print("No more character present to form subsequence")
                    return False

                subsequence_i = s2.index(s1[i])

                if 0 <= subsequence_i < len(s2)-1:
                    while indices[s2[subsequence_i+1]] and indices[s2[subsequence_i+1]][0] < indices[s2[subsequence_i]][0]:
                        delete_index = indices[s2[subsequence_i+1]].popleft()
                        print(f"{delete_index} can't produce a subsequence, removing it")
                        s1_exists[delete_index] = False
                    
                    if not indices[s2[subsequence_i+1]]:
                        print(indices)
                        print("Next element not there")
                        return False
                    
                if 0 < subsequence_i <= len(s2)-1:
                    while indices[s2[subsequence_i-1]] and indices[s2[subsequence_i-1]][0] > indices[s2[subsequence_i]][0]:
                        delete_index = indices[s2[subsequence_i-1]].popleft()
                        print(f"{delete_index} can't produce a subsequence, removing it")
                        s1_exists[delete_index] = False
                    
                    if not indices[s2[subsequence_i-1]]:
                        print("Previous element not there")
                        return False
                    
                s1_exists[i] = False
            else:
                print(f"Already removed {s1[i]}")


        print(indices)
        print(s1_exists)

        return True
    
    ans = 0

    for i in range(len(start)):
        
        print("Deleting range", start[i], end[i])
        if delete_range(start[i], end[i]):
            print("Possible to form subsequence")
            ans += 1
        else:
            print("Cant form subsequence")
            return ans

    return ans


print(findDaysS2SubsequenceOfS1("abcdefghabc", "abc", [0, 0, 1, 2, 9], [1, 2, 3, 3, 10]))