
s = "(tne(cell)xe)"


def reverse_string_in_parentheses(s: str) -> str:
    i = 0
    n = len(s)
    stk = ['']

    while i < n:
        if s[i].isalpha():
            stk[-1] += s[i]
        elif s[i] == '(':
            stk += '',
        elif s[i] == ')':
            cur = stk.pop()
            if stk:
                stk[-1] += cur[::-1]
            else:
                stk += cur[::-1]
        i += 1

    return ''.join(stk)


print("excellent" == reverse_string_in_parentheses(s))