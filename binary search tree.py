import random


class myNode(object):
    def __init__(self, v=0):
        self.previous = None
        self.next = None
        self.val = v


class myTree(object):
    def __init__(self):
        self.root = myNode(250)#root'a 250 eklendi


def inorder(root):
    if root:
        inorder(root.previous)#root'un öncesi
        print(root.val, end=' ')
        inorder(root.next)#root'un sonrası


def insert_1(root, node):
    if (root is None):#kök bos ise
        root = node
    else:
        if (root.val < node.val):
            if (root.next is None):
                root.next = node
            else:
                insert_1(root.next, node)
        else:
            if (root.previous is None):
                root.previous = node
            else:
                insert_1(root.previous, node)
                import random


def test():
    numbers = []
    for x in range(5):#5 sayı ekleniyor
        numbers.append(random.randint(1, 101))
    numbers
    tree_1 = myTree()
    for n in numbers:
        insert_1(tree_1.root, myNode(n))
    inorder(tree_1.root)


test()