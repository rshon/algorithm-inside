import collections


nums = [1, 2, 1, 2, 1]
k = 3


def get_num_subarray(nums: [int], k: int) -> int:
    tot = 0
    idxs = collections.defaultdict(int)
    idxs[0] = 1
    cnt = 0
    
    for num in nums:
        tot += num
        if tot - k in idxs:
            cnt += idxs[tot - k]
        
        idxs[tot] += 1
    
    return cnt


assert(4 == get_num_subarray(nums, k))