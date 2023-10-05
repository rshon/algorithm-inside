import collections


emails = [["Tim", "timothy@mail.com", "timo21k@mail.com"], ["Tim", "timjackson@mail.com"], ["Blige", "blige@mail.com"], ["Tim", "timo21k@mail.com", "tim_seoul@mail.com"]]


def merge_email_accounts(emails):
    g = collections.defaultdict(set)
    names = collections.defaultdict(str)

    for acc in emails:
        for i in range(1, len(acc)):  # 1 for only email case
            g[acc[1]].add(acc[i])
            g[acc[i]].add(acc[1])

        names[acc[1]] = acc[0]

    visited = set()
    res = []

    for email in g:
        if email in visited:
            continue

        q = collections.deque([email])
        visited.add(email)
        linked_emails = [email]

        while q:
            u_email = q.popleft()

            for v_email in g[u_email]:
                if v_email in visited:
                    continue

                visited.add(v_email)
                linked_emails += v_email,
                q += v_email,

        res += [names[email]] + sorted(linked_emails),

    return res


print(merge_email_accounts(emails))