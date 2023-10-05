
s = "())("


def find_min_parentheses(s: str) -> int:
    stk = []
    for ch in s:
        if stk and (stk[-1] == '(' and ch == ')'):
            stk.pop()
            continue

        stk += ch,
    
    return len(stk)


print(2 == find_min_parentheses(s))