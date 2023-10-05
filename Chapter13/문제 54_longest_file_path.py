
def get_longest_abs_path(s: str) -> int:
    lines = s.split('\n')
    stk = []
    mx = 0

    for line in lines:
        depth = line.count('\t')

        while stk and len(stk) > depth:
            stk.pop()

        line = line.replace('\t', '')
        stk += line,

        if '.' in line:
            mx = max(mx, len('/'.join(stk)))

    return mx


print(42 == get_longest_abs_path("root_dir\n\tdepth1_dir1\n\t\tfile1.ext\n\tdepth1_dir2\n\t\tfile2.ext\n\t\tdepth2_dir1\n\t\t\tfile3.ext"))
