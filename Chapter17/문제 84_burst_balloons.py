from typing import List


def get_max_score(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    
    def dfs(l, r):
        if (l, r) in mem:
            return mem[(l, r)]

        if l > r:
            return 0

        mx = 0
        for i in range(l + 1, r):
            mx = max(mx, nums[l]*nums[i]*nums[r] + dfs(l, i) + dfs(i, r))
        
        mem[(l, r)] = mx
        return mx
   
    mem = {} 
    return dfs(0, len(nums) - 1)


balloons = [2, 5, 3, 1]
res = get_max_score(balloons)
print(res)
