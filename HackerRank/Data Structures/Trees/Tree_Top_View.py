'''
HackerRank
Tree: Top View
https://www.hackerrank.com/challenges/tree-top-view/problem
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


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def vo_traversal(root, columns={}, n=0):
    if root == None:
        return
    if n in columns:
        columns[n].append(root)
    else:
        columns[n] = [root]
    vo_traversal(root.left, columns, n - 1)
    vo_traversal(root.right, columns, n + 1)
    vo = {}
    for i in sorted(columns):
        if i in vo:
            vo[i].append(columns[i])
        else:
            vo[i] = columns[i]
    return vo


def topView(root):
    # Write your code here
    # level order traversal
    level_order = []
    queue = [root]
    while queue:
        cur = queue.pop()
        level_order.append(cur)
        if cur.left:
            queue.insert(0, cur.left)
        if cur.right:
            queue.insert(0, cur.right)

    # vertical order traversal
    columns = vo_traversal(root)
    for i in columns:
        if len(columns[i]) == 1:
            print(columns[i][0].info, end=' ')
        else:
            n = []
            for j in columns[i]:
                n.append(level_order.index(j))

            print(level_order[min(n)].info, end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)