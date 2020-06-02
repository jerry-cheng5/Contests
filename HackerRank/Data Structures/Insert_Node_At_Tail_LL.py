'''
HackerRank
Insert a Node at the Tail of a Linked List
https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
Jerry Cheng
'''

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

def insertNodeAtTail(head, data):
    temp = SinglyLinkedListNode(data)
    if head == None:
        head = temp
        return head
    else:
        cur_node = head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = temp
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
