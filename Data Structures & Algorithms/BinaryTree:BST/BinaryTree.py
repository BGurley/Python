#Brandon Gurley
#October 17th 2022
#CIS 360
#Lab 5

class BinaryTreeNode:
    def __init__(self, data):
        self.left = None # Left Child
        self.right = None # Right Child
        self.data = data # Node Data

    def insertion(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insertion(data)
            elif data>self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insertion(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            leftPrint = self.left.data
        else:
            leftPrint = 'e'
        if self.right:
            self.right.PrintTree()
            rightPrint = self.right.data
        else:
            rightPrint = 'e'
        print('{}({},{})'.format(self.data, leftPrint, rightPrint))
    def height(root, counter):
        if root.left == None:
            leftDepth = counter
        else:
            leftDepth = root.left.height(counter+1)


        if root.right == None:
            rightDepth = counter
        else:
            rightDepth = root.right.height(counter+1)
        if leftDepth > rightDepth:
            return leftDepth
        else:
            return rightDepth

    def rangePrint(self, k1, k2):
        if self.left:
            self.left.rangePrint(k1, k2)

        if self.right:
            self.right.rangePrint(k1, k2)

        if self.data >= k1 and self.data <= k2:
            print(self.data)

    def getN(root):
        if root.left == None:
            left = 0
        else:
            left = root.left.getN()
        if root.right == None:
            right = 0
        else:
            right = (root.right.getN())
        return (left+right+1)

    def TreeSelect(root, i):
        w = root.left
        #print(i)
        #print(w.getN())
        if w == None:
            nW = 0
        else:
            nW = w.getN()
        if i <= nW:
            return w.TreeSelect(i)
        elif i == (nW+1):
            return root
        else:
            return root.right.TreeSelect((i-nW-1))
print("Please enter your integer input, separated by commas")
inputValues = input()
array = [int(x) for x in inputValues.split(',') if x.isdigit()]
#array = [6,4,8,2,7,3,1]
root = BinaryTreeNode(array[0])
n = len(array)
for i in range(1,n):
    root.insertion(array[i])
root.PrintTree()
print(root.height(0))
root.rangePrint(4, 8)
print('Get N: ' , root.getN())
print(root.TreeSelect(3).data)
#print(inputValues)
