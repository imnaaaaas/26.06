"""
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)
"""

""" with memoization
cache={}
def fib(n):
    if n in cache:
        return cache[n] #if n exsist in cache
    if n<=1:
        return 1
    cache[n]=fib(n-1)+fib(n-2) #fill cache with neeeded
    return cache[n] #return 
"""

""" tabulation
def fib(n):
    if n<=1:
        return n
    table = [0]*(n+1) #base cases
    table[0]=0
    table[1]=1
    for i in range(2,n+1): #2 to n fill linear
        table[i]=table[i-1]+table[i-2]
    return table[n]#final last item

print(fib(8))
"""






""" tabulation coin_change

def coin_change(coins,amount):
    dp=[amount+1]*(amount+1) #initialization
    dp[0]=0#base first
    for i in range(1,amount+1): #from 1 to our target number
        for coin in coins:
            if i-coin>=0: #tu chixi ar ari
                dp[i]=min(dp[i],dp[i-coin]+1) #if we get better deal with that coin
    return dp[amount] if dp[amount]!=amount+1 else -1 #if amount is unreachable and if it is return -1
print(coin_change([1,2,3,4,5], 11))
"""





""" memoization choin_change
def coin_change(coins,amount):
    cache = {}
    def solve(remaining):
        if remaining==0: return 0 #chixi
        if remaining <0: return float('inf')#chixi
         
        if remaining in cache: #overlapping sub-problem if already exsist
            return cache[remaining]
        min_coins=float('inf')  

        for coin in coins: #optimal structure
            res=solve(remaining-coin)#monetis agebis shemdeg darchenili tanxa solvshi midis
            if res!= float('inf'):#if not chixi
                min_coins=min(min_coins,res+1) #check if it exsist or new 
        cache[remaining]=min_coins #best answer saved
        return cache[remaining] #return minimal answer
    result = solve(amount) #start recursion with begin remaining
    return result if result!= float('inf') else -1 #if asnwer is unreachable or return -1

print(coin_change([1, 2, 5,9], 11))
"""



""" house rob
def rob_mem(nums):
    cache={}
    def solve(i):
        if i>=len(nums): #if we are in last house
            return 0
        if i in cache:
            return cache[i]
        rob_it = nums[i] + solve(i+2)#rob this and skip next house
        skip_it=solve(i+1)#skip [0] and start from[1]
        cache[i]=max(rob_it,skip_it) #find max
        return cache[i]
    return solve(0)

print(rob_mem([2, 7, 9, 3, 1]))
"""


def rob(nums):
    if not nums: return 0
    if len(nums)==1: return nums[0]

    dp=[0] *len(nums) #array to store max
    dp[0]=nums[0] #base case
    dp[1]=max(nums[0], nums[1]) #choose 1 or 2
    for i in range(2, len(nums)):
        dp[i]= max(nums[i] + dp[i-2],dp[i-1]) #rob max or skip
    return dp[-1] #last element in array

print(rob([2, 7, 9, 3, 1]))



