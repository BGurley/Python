#Brandon Gurley


class Node:
  def __init__(self, data):
    self.data = data

parent = {}
def makeSet(set):
    for x in set:
        x.parent = x
        x.size = 1

def find(x):
    r = x
    while r.parent != r:
        r = r.parent
    return r

def getDepth(x):
    r = x
    counter = 0
    while r.parent != r:
        r = r.parent
        counter += 1
    return counter

def union(x, y):
    x.parent = y
    y.size = (y.size+x.size)


#set of stuffs
set = []

for i in range (0,50):
    x = Node(i)
    set.append(x)

print(makeSet(set))

for i in range (0,45):
    union(find(set[i]), find(set[i+5]))

for i in range(0, 50):
    print(set[i].data, find(set[i]).data, getDepth(set[i]))


print(set[1].parent)
