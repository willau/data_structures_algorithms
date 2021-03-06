# encoding: utf-8
"""
author: willy au
date: 16 Nov. 2017

Binary search tree <-> BST
Time complexity of BST sort algorithm:
    + Average -> O(n.log(n))
    + Worst   -> O(n^2)

Space complexity, tree takes O(n) space:
    + O(n)

Bug encountered:
    + self.root = None, does not work
        + Cause: reference to self.root is lost
        + Consequence: insert_at_node replace None by None
        + Solution:
            + use a function 'isnull()' to create null node
            + use the fact that class can be referenced
    + remember to use 'None' with cautious next time
"""


def tree_sort(array):
    bstree = BSTree()
    for e in array:
        bstree.insert(e)
    array = list()
    inorder_traverse(bstree.root, array)
    return array


def inorder_traverse(node, array):
    if node.left is not None:
        inorder_traverse(node.left, array)
    array.append(node.data)
    if node.right is not None:
        inorder_traverse(node.right, array)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def isnull(self):
        return (self.data is None)


class BSTree:
    def __init__(self):
        self.root = Node()
        self.array = list()

    def insert_at_node(self, node, data):
        if node.isnull():
            node.data = data
        else:
            if data >= node.data:
                if node.right is None:
                    node.right = Node()
                self.insert_at_node(node.right, data)
            else:
                if node.left is None:
                    node.left = Node()
                self.insert_at_node(node.left, data)

    def insert(self, data):
        self.insert_at_node(self.root, data)

