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


""" coin_change
def coin_change(coins,amount):
    dp=[amount+1]*(amount+1) #initialization
    dp[0]=0#base first
    for i in range(1,amount+1): #from 1 to our target number
        for coin in coins:
            if i-coin>=0: #tu chixi ar ari
                dp[i]=min(dp[i],dp[i-coin]+1) #if we get better deal with that coin
    return dp[amount] if dp[amount]!=amount+1 else -1 #if amount is unreachable and if it is return -1
print(coin_change([1,2,3,4,5], 11))



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

""" rob memoization
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
    return solve(0)#top-down

print(rob_mem([2, 7, 9, 3, 1]))
"""


""" rob tabulation
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
"""


""" palindrome
def is_pal(name):
    left=0
    right=len(name)-1
    while left<right:
        if name[left] != name[right]:
            return False
        else:
            left+=1
            right-=1
    return True

print(is_pal("asdasd"))
"""

"""climb_stairs
def climb_stairs(n):
    cache={}
    def solve(i):
        if i < 0: 
            return 0
        if i == 0 or i == 1: 
            return 1
        if i in cache:
            return cache[i]
        cache[i]=solve(i-1)+solve(i-2)
        return cache[i]
    return solve(n)

          



def climb_stairs2(n):
    if n<=1:
        return 1
    table=[0]*(n+1)
    table[0]=1
    table[1]=1
    for i in range(2, n+1):
        table[i]=table[i-1]+table[i-2]
    return table[i]

print(climb_stairs2(5))
"""     


""" find max D&C
def find_max(nums):
    if not nums:
        return None
    return find_max_dc(nums, 0 , len(nums)-1)

def find_max_dc(nums, low, high):
    if low == high:
        return nums[low]
    mid=(low+high)//2 #devide
    left_max=find_max_dc(nums,low,mid)#conquer
    right_max=find_max_dc(nums,mid +1, high)#conquer
    if left_max>right_max:
        return left_max
    else:
        return right_max

print(find_max([1,2,3,465, 32,12,15,67]))
"""


""" D&C quick_sort
def quick_sort(nums):
    if len(nums) <=1:
        return nums
    pivot=nums[len(nums)//2]
    left= [x for x in nums if x< pivot]
    mid = [x for x in nums if x ==pivot]
    right = [x for x in nums if x>pivot]
    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([1,4,5,2,6,9,64,2,6]))

"""



""" #pascal triangle

def method(n):
    if n==0:
        return []
    if n==1:
        return [[1]]
    lastRow=method(n-1)#get last rows
    newRow=[1]*n #fills new rows with 1
    for i in range(1,n-1): #get from first index and last index -1
        newRow[i]=lastRow[-1][i-1]+lastRow[-1][i] #get sum of middle numbrs
    lastRow.append(newRow)
    return lastRow
print(method(5))


def method(n):
    res=[1]
    for i in range(n):
        newRow=[0]*(len(res)+1) #new rowbigger thanbefore 
        for j in range(len(res)): #every num on prevRow
            newRow[j]+=res[j] #add num on left 
            newRow[j+1]+=res[j] #add same num onright
        res=newRow
    return res
print(method(3))
"""


""" from triangle choose min sum

def triangle_min(triangle):
    for i in range(len(triangle)-2,-1,-1):#start,stop,step bottom top
        for j in range(len(triangle[i])):#goes each row
            triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1]) #add min from left and right
    return triangle[0][0]

print(triangle_min([[2],[3,4],[6,5,7],[4,1,8,3]]))
"""

def is_subsequence(s,t):
    i=0
    for j in t:
        if j == s[i]:
            i+=1
        if i==len(s):
            return True
    return False

print(is_subsequence("ki", "giokirgi"))