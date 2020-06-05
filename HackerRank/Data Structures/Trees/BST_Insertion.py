'''
HackerRank
Binary Search Tree: Insertion
https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
Jerry Cheng
'''

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # Enter you code here
        node = Node(val)
        if self.root == None:
            self.root = node
            return self.root

        cur = self.root
        while cur:
            if val < cur.info:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    break
            elif val > cur.info:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    break
        return self.root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
