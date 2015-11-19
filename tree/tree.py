# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '15-11-18'


class Node(object):
    """节点类"""

    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data):
        self.left_child = Tree(data)
        return self.left_child

    def insert_right(self, data):
        self.right_child = Tree(data)
        return self.right_child

    def print_data(self):
        print(self.data, end="")

    """前序遍历"""

    @staticmethod
    def dlr(node):
        if node.data:
            node.print_data()
            if node.left_child:
                Tree.dlr(node.left_child)
            if node.right_child:
                Tree.dlr(node.right_child)

    """中序遍历"""

    @staticmethod
    def ldr(node):
        if node.data:
            if node.left_child:
                Tree.ldr(node.left_child)
            node.print_data()
            if node.right_child:
                Tree.ldr(node.right_child)

    """后序遍历"""

    @staticmethod
    def lrd(node):
        if node.data:
            if node.left_child:
                Tree.ldr(node.left_child)
            if node.right_child:
                Tree.ldr(node.right_child)
            node.print_data()


if __name__ == '__main__':
    root = Tree('A')
    B = root.insert_left('B')
    C = root.insert_right('C')
    D = B.insert_left('D')
    E = B.insert_right('E')
    F = D.insert_left('F')
    G = C.insert_left('G')
    H = C.insert_right('H')
    I = G.insert_left('I')
    K = I.insert_left('K')
    J = H.insert_right('J')
    L = J.insert_left('L')

    Tree.dlr(root)
    print()
    Tree.ldr(root)
    print()
    Tree.lrd(root)
