import collections


nums1 = [3, 5]
nums2 = [5, 1, 7]
k = 4


def pick_max_numbers(nums1, nums2, k):
    def lds(nums, k):
        remain = n = len(nums)
        stk = collections.deque([])

        for num in nums:
            while stk and stk[-1] < num and remain > k:
                stk.pop()
                k += 1

            if k:
                stk += num,
                k -= 1

            remain -= 1

        return stk

    def comp(seq1, seq2):
        n = max(len(seq1), len(seq2))

        for i in range(n):
            if i < len(seq1) and i < len(seq2):
                if seq1[i] > seq2[i]:
                    return 1
                elif seq1[i] < seq2[i]:
                    return -1
            elif i < len(seq1):
                return 1
            else:
                return -1

        return 0

    def merge(seq1, seq2):
        res = []

        while seq1 or seq2:
            if 1 == comp(seq1, seq2):
                res += seq1.popleft(),
            else:
                res += seq2.popleft(),
          
        return res

    res = []

    for i in range(k + 1):
        if i > len(nums1) or (k - i) > len(nums2):
            continue

        seq = merge(lds(nums1, i), lds(nums2, (k - i)))
        res = max(res, seq)

    return res


assert([5, 7, 3, 5] == pick_max_numbers(nums1, nums2, k))