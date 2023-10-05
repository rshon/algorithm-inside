from types import List


def get_max_length_of_sub_array(nums: List[int]) -> int:
    inc = mx = float('-inf')
    
    for num in nums:
        inc = max(num, inc + num)
        mx = max(mx, inc)
    
    return mx
