import random

class Node:

    def __init__(self, val):
        self.value = int(val)
        self.left = None
        self.right = None

    def add_left(self, l):
        self.left = l

    def add_right(self, r):
        self.right = r

    def remove_left(self):
        self.left = None

    def remove_right(self):
        self.right = None


def add_rand(root, node):
    direction = random.randint(0, 1)
    if direction == 0:
        if root.left == None:
            root.add_left(node)
        else:
            add_rand(root.left, node)
    else:
        if root.right == None:
            root.add_right(node)
        else:
            add_rand(root.right, node)