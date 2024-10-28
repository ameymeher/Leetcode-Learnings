# Sliding window tips

## Tips to spot the pattern:
1. A variable sized window needs to be maintained
2. There should be a validity check of the window
3. Sometimes a problem might not seem a sliding window problem because of the confusion of when to shift l
4. In some cases, it is possible to frame a sliding window approach, imposing some constraints and then solving the original problem. Example [Longest Substring with At Least K Repeating Characters](./Longest%20Substring%20with%20At%20Most%20Two%20Distinct%20Characters.py)


## Coding Structure:
1. Incrementing the right pointer through a loop
2. Inculcating the right pointer data
3. Logic to shift the left pointer
    1. l <= r check
    2. The valid window check
4. Update the answer after checking the validity of the window once and using the length of the current valid window if there is one. l<=r ensures that if a current window is not valid, the length is 0 here.