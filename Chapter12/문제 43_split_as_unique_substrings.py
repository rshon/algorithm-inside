
def split_max_unique_substring(s: str) -> int:
    n = len(s)

    def dfs(start, visited): 
        if start == n:
            return 0

        mx = 0
        for cur in range(start + 1, n + 1):
            word = s[start:cur]
            if word in visited:
                continue

            visited.add(word)
            mx = max(mx, 1 + dfs(cur, visited))
            visited.discard(word)

        return mx 
        
    return dfs(0, set())


print(5 == split_max_unique_substring("wwwffhww"))