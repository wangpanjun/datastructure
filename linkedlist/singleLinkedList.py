# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '19/11/15'

"""节点类"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nex = None


class LinkedList(object):
    def __init__(self):
        """初始化链表"""
        self.head = None

    """获取链表长度"""

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.nex
        return length

    """判断链表是否为空"""

    def is_empty(self):
        return False if len(self) > 0 else True

    """追加节点"""

    def append(self, data):
        """
        1.head 为none :head-->node
        2.tail.nex-->node
        :param data:
        :return:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            pre = self.head
            while pre.nex:
                pre = pre.nex
            pre.nex = node

    """插入节点"""

    def insert(self, index, data):
        """
        1.index 插入节点位置包括正负数
        2.找到index-1-->pre_node的节点
        3.pre_node.next-->node
          node.next-->pre_node.next.next
        4.head
        :param index:
        :param data:
        :return:
        """
        node = Node(data)
        if abs(index + 1) > len(self):
            return False
        index = index if index >= 0 else len(self) + index + 1
        if index == 0:
            node.nex = self.head
            self.head = node
        else:
            pre = self.get(index - 1)
            if pre:
                nex = pre.nex
                pre.nex = node
                node.nex = nex
            else:
                return False
        return node

    """反转链表"""

    def __reversed__(self):
        """
        1.pre-->next 转变为 next-->pre
        2.pre 若是head 则把 pre.nex --> None
        3.tail-->self.head
        :return:
        """

        def reverse(pre_node, node):
            if pre_node is self.head:
                pre_node.nex = None
            if node:
                next_node = node.nex
                node.nex = pre_node
                return reverse(node, next_node)
            else:
                self.head = pre_node

        return reverse(self.head, self.head.nex)

    """获取节点"""

    def get(self, index):
        """
        :param index:
        :return:
        """
        index = index if index >= 0 else len(self) + index
        if len(self) < index or index < 0:
            return None
        pre = self.head
        while index:
            pre = pre.nex
            index -= 1
        return pre

    """设置节点"""

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        return node

    """删除某个元素"""

    def delete(self, index):
        f = index if index > 0 else abs(index + 1)
        if len(self) <= f:
            return False
        pre = self.head
        index = index if index >= 0 else len(self) + index
        prep = None
        while index:
            prep = pre
            pre = pre.nex
            index -= 1
        if not prep:
            self.head = pre.nex
        else:
            prep.nex = pre.nex
        return pre.data

    """清空链表"""

    def clear(self):
        self.head = None

    """打印链表"""

    def show(self):
        pre = self.head
        while pre:
            print(pre.data, end=" ")
            pre = pre.nex
        print()


if __name__ == '__main__':
    ls = LinkedList()
    ls.append(1)
    ls.append(2)
    ls.append(3)
    ls.insert(-1, 10)
    ls.show()
    print(ls.get(-1).data)
    reversed(ls)
    ls.show()
    print(ls.get(0).data)
    ls.show()
    ls.delete(2)
    ls.show()
    ls.set(-12, 20)
    ls.show()
