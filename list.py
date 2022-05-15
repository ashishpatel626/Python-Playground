x = []
y = []
for i in range(11):
    x.insert(i, i)
    y.insert(i, 'a')

#x.reverse()
#min(x)
#max(x)
#x.insert(4, 9)
#x.sort()
#x.clear()
#x.count(2)
#x.index(2)
#len(x)
#x.pop(0)
#x.append(2)
#x.extend(y)

if 3 in x:
    print(x.index(3))
else:
    print("not found")

