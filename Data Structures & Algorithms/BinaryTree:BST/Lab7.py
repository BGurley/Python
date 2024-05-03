#Brandon Gurley


class Node:
  def __init__(self, data):
    self.data = data

class DoinStuff:

    parent = {}

    def makeSet(self, set):
        for x in set:
            x.parent = x
            x.size = 1

    def find(x):
        r = x
        while r.parent != r:
            r = r.parent
        z = x
        while z.parent != z: #find the root, delete for part 2
            w = z
            z = z.parent
            w.parent = r

    def union(x, y):
        if x.size < y.size:
            x.parent = y
            y.size = (y.size+x.size)
        else:
            y.parent = x
            x.size = (x.size+y.size)


#set of stuffs
set = []

for i in range (0,5):
    x = Node(i)
    set.append(x)


#setup the class for ez usage
stuff = DoinStuff()

print(stuff.makeSet(set))
print(set[1].parent)
