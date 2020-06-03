'''
HackerRank
Inserting a Node Into a Sorted Doubly Linked List
https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
Jerry Cheng
'''

# !/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the sortedInsert function below.

def sortedInsert(head, data):
    cur = head
    node = DoublyLinkedListNode(data)
    while cur.next != None:
        if data <= cur.data:
            break
        cur = cur.next

    if cur.next == None and data > cur.data:
        node.prev = cur
        cur.next = node
    else:
        prev = cur.prev
        node.next = cur
        node.prev = prev
        cur.prev = node
        if prev != None:
            prev.next = node
        else:
            head = node
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
