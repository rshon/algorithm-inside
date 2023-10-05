import re


res = re.search('Python', 'Python world!')
print(res)
print(res.span()[0], res.span()[1])

res = re.match('Sneak', 'Python world!')
print(res)

res = re.search('Python', '-Python world!')
print(res)

res = re.match('Python', '-Python world!')
print(res)

res = re.match('[A-Z]+', ' AAbc world!')
print(res)

res = re.search('[A-Z]+', ' AAbc world!')
print(res)
print(res.span()[0], res.span()[1])

res = re.search('^[A-Z]+', ' AAbc world!')
print(res)

res = re.search('^[A-Z]+', 'AAbc world!')
print(res)
print(res.span()[0], res.span()[1])

res = re.search('[^A-Z]+', 'AAbc world!')
print(res)
print(res.span()[0], res.span()[1])

res = re.match('[a-z.]+', 'python.world@abcde.com')
print(res)
print(res.span()[0], res.span()[1])

res = re.match('[a-z.]+', 'python.world001@abcde.com')
print(res)
print(res.span()[0], res.span()[1])

res = re.match('[a-z.0-9]+', 'python.world001@abcde.com')
print(res)
print(res.span()[0], res.span()[1])

res = re.match('[\w.]+', 'python.world001@abcde.com')
print(res)
print(res.span()[0], res.span()[1])

res = re.match('([\w.]+)@([\w.]+)', 'python.world001@abcde.com')
print(res)
print(res.span()[0], res.span()[1])

print(res.groups())
print(res.group(0))
print(res.group(1))
