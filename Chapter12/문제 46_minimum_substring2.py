import collections


s = "bdab"
t = "ab"


def find_min_substring(s: str, t: str) -> str:
    req = collections.Counter(t)
    wnd = collections.defaultdict(int)
    num_kind = 0
    
    l = r = 0
    mn = float('inf')
    ml = mr = 0
    
    while r < len(s):
        if s[r] not in t:
            r += 1
            continue
        
        wnd[s[r]] += 1
        
        if wnd[s[r]] == req[s[r]]:
            num_kind += 1
        
        while l <= r and num_kind == len(req):
            if s[l] not in t:
                l += 1
                continue
                
            if mn > r - l  + 1:
                mn = r - l + 1
                ml = l
                mr = r

            wnd[s[l]] -= 1
            if wnd[s[l]] < req[s[l]]:
                num_kind -= 1
            
            l += 1
        
        r += 1
    
    return s[ml:mr + 1] if mn != float('inf') else ''


print(find_min_substring(s, t))