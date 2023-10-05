
n = 573

def make_increasing_sequence(n: int) -> int:
    nums = list(map(int, str(n)))
    prev = []
    
    while True:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i] -= 1
                nums[i + 1:] = [9]*(len(nums) - (i + 1))
        
        if prev == nums:
            break
        
        prev = nums[:]
    
    return int(''.join([str(num) for num in nums]))


print(569 == make_increasing_sequence(n))

