# Python 实现单向链表

------



## 什么是 **链表**

链表顾名思义就是～链
链表是一种动态数据结构，他的特点是用一组任意的存储单元存放数据元素。链表中每一个元素成为“结点”，每一个结点都是由数据域和指针域组成的。跟数组不同链表不用预先定义大小，而且硬件支持的话可以无限扩展。

###链表与数组的不同点：

 1. 数组需要预先定义大小，无法适应数据动态地增减，数据小于定义的长度会浪费内存，数据超过预定义的长度无法插入。而链表是动态增删数据，可以随意增加。
 2. 数组适用于获取元素的操作，直接get索引即可，链表对于获取元素比较麻烦需要从头一直寻找，但是适用与增删，直接修改节点的指向即可，但是对于数组就比较麻烦了，例如［1，2，3，4］需要在下标为1的位置插入－2，则需要将［2，3，4］后移，赋值ls[1]=-2
 3. 数组从栈中分配空间, 对于程序员方便快速,但自由度小。链表从堆中分配空间, 自由度大但申请管理比较麻烦.

### 单向链表

### 链表基本方法实现（Python）

### 1. 初始化链表
```
"""节点类"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nex = None

def __init__(self):
    """初始化链表"""
    self.head = None
```

### 2. 获取链表长度
```
def __len__(self):
    pre = self.head
    length = 0
    while pre:
        length += 1
        pre = pre.nex
    return length
```

### 3. 追加节点
追加节点还是比较简单的,如果head节点不存在，则当前节点为head节点，否则的话找到尾节点，将尾节点的next指向当前节点（可以添加head和tail两个节点，就不用递归寻找尾节点了）
![追加节点](http://img.blog.csdn.net/20151119233848487)
```
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
```

### 4. 获取节点
获取节点也是比较容易的，无非就是判断index值的正负
```
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
```
### 5. 设置节点
找到当前节点赋值即可
```
"""设置节点"""

def set(self, index, data):
    node = self.get(index)
    if node:
        node.data = data
    return node
```
### 6. 插入节点
插入节点需要找到插入节点的前一个节点pre_node（索引index的正负，前一节点不同，需要判断一下），然后将pre_node.nex指向当前节点。同时将当前节点的nex指向pre_node.nex.nex
![插入节点](http://img.blog.csdn.net/20151119233548930)
```
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
```
### 7. 删除节点
删除节点，也要区分一下索引的正负。找到当前节点的前一个节点pre_node和后一个节点next_node，将pre_node.nex-->next_node即可
![删除节点](http://img.blog.csdn.net/20151120112608565)
```
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
```

### 8. 反转链表
反转链表的实现有多种方式，比较简单的就是生成一个新的链表－－》可以用数组存储所有节点让后倒序生成新的链表
在这里用下面这种方式生产：
反转链表就是将node.nex-->pre_node 递归实现即可，然后让tail赋值为head
![反转链表](http://img.blog.csdn.net/20151119233824408)
```
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
```
### 9. 清空链表
将头赋为空就好
```
"""清空链表"""

def clear(self):
    self.head = None
```

