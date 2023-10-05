
s1 = "sjua"
s2 = "eeku"
s3 = "sjeuekau"


def interleave(s1: str, s2: str, s3: str) -> bool:
    n = len(s1)
    m = len(s2)
    
    if n + m > len(s3):
        return False
    
    def check(i, j, inter):
        if inter and inter[-1] != s3[len(inter) - 1]:
            return False
        
        if i == n and j == m:
            return inter == s3
        
        res = False
        if i < n:
            res = res or check(i + 1, j, inter + s1[i])
        
        if j < m:
            res = res or check(i, j + 1, inter + s2[j])
        
        return res
    
    return check(0, 0, '')


print(interleave(s1, s2, s3))