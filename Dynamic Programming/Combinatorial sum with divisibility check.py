"""
Faced in Tiktok assessment:

TikTok Credits Distribution Challenge In the grand finale of a prestigious TikTok tournament, the organizers have prepared several boxes filled with TikTok credits as prizes for the participants. 
They know exactly how many participants will compete in the tournament and want to ensure that every participant receives an equal number of TikTok credits to avoid any disappointment. 
Once a box is opened, all the credits inside it must be distributed. 
You need to find all distinct ways to select credit boxes such that the total sum of credits in each combination can be evenly distributed among P participants. 
If no such combinationg exist, return 0. Return the result modulo 10^9+7. 
Example Input participants = 6 credits = [12, 18, 24, 36) Output: 15 
give code in python

Let dp[i] represent the number of ways to achieve a sum of i modulo P. 
Initialize dp[0] = 1 because there is one way to achieve a sum of 0 (by choosing no boxes).
"""

def count_combinations(participants, credits):
    MOD = 10**9 + 7
    P = participants
    dp = [0] * P
    dp[0] = 1
    
    for credit in credits:
        for i in range(P - 1, -1, -1):
            dp[(i + credit) % P] = (dp[(i + credit) % P] + dp[i]) % MOD
    
    return sum(dp[i] for i in range(0, P, P)) % MOD

# Example usage
participants = 6
credits = [7, 8, 9, 7]
print(count_combinations(participants, credits)-1)  # Output: 15