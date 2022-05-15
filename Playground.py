import sys
a = 'my-string'


d = [a]
l = sys.getrefcount(a)

print(l)