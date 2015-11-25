# Python 实现单向链表（图解）

------





## 双向链表


双向链表也叫双链表，是链表的一种，它的每个数据结点中都有两个指针，分别指向直接后继和直接前驱。所以，从双向链表中的任意一个结点开始，都可以很方便地访问它的前驱结点和后继结点。

## 双向链表基本方法实现（Python）
### 1. 初始化链表
定义节点结构：指针域pre、next和数据域data
为方便操作添加了head和tail节点，初始化时head.next-->tail,tail.pre-->next
```
"""节点类"""
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None

"""初始化双向链表"""

def __init__(self):
    """
    设置头尾，操作比较容易
    头－－（next）－－》尾
    尾－－（pre）－－》头
    :return:
    """
    head = Node()
    tail = Node()
    self.head = head
    self.tail = tail
    self.head.next = self.tail
    self.tail.pre = self.head
```
![初始化](http://img.blog.csdn.net/20151120150312185)
### 2. 获取链表长度
起始head，每有一个节点，length＋1
```
"""获取链表长度"""

def __len__(self):
    length = 0
    node = self.head
    while node.next != self.tail:
        length += 1
        node = node.next
    return length
```

### 3. 追加节点
因为有tail 节点，所以找到tail.pre 节点就好了
```
"""追加节点"""

def append(self, data):
    """
    :param data:
    :return:
    """
    node = Node(data)
    pre = self.tail.pre
    pre.next = node
    node.pre = pre
    self.tail.pre = node
    node.next = self.tail
    return node
```
![追加节点](http://img.blog.csdn.net/20151120150212210)
### 4. 获取节点
获取节点要判断index正负值
```
 """获取节点"""
def get(self, index):
    """
    获取第index个值，若index>0正向获取else 反向获取
    :param index:
    :return:
    """
    length = len(self)
    index = index if index >= 0 else length + index
    if index >= length or index < 0: return None
    node = self.head.next
    while index:
        node = node.next
        index -= 1
    return node
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
插入节点需要找到插入节点的前一个节点pre_node和后一个节点next_node（索引index的正负，前一节点不同，需要判断一下），然后将pre_node.next-->node,node.pre->pre_node;next_node.pre-->node,node.next-->next_node
```
"""插入节点"""

def insert(self, index, data):
    """
    因为加了头尾节点所以获取节点node就一定存在node.next 和 node.pre
    :param index:
    :param data:
    :return:
    """
    length = len(self)
    if abs(index + 1) > length:
        return False
    index = index if index >= 0 else index + 1 + length

    next_node = self.get(index)
    if next_node:
        node = Node(data)
        pre_node = next_node.pre
        pre_node.next = node
        node.pre = pre_node
        node.next = next_node
        next_node.pre = node
        return node

```
![插入节点](http://img.blog.csdn.net/20151120150250201)
### 7. 删除节点
删除节点，也要区分一下索引的正负。找到当前节点的前一个节点pre_node和后一个节点next_node，将pre_node.nex-->next_node即可
```
"""删除节点"""

def delete(self, index):
    node = self.get(index)
    if node:
        node.pre.next = node.next
        node.next.pre = node.pre
        return True

    return False
```
![删除节点](http://img.blog.csdn.net/20151120150227911)
### 8. 反转链表
反转链表的实现有多种方式，比较简单的就是生成一个新的链表－－》可以用数组存储所有节点让后倒序生成新的链表
在这里用下面这种方式生产：
可能有点绕
 1.node.next --> node.pre；node.pre --> node.next（递归）
 2.head.next --> None；tail.pre --> None
 3.head-->tail；tail-->head
```
"""反转链表"""
def __reversed__(self):
    """
    1.node.next --> node.pre
      node.pre --> node.next
    2.head.next --> None
      tail.pre --> None
    3.head-->tail
     tail-->head
    :return:
    """
    pre_head = self.head
    tail = self.tail

    def reverse(pre_node, node):
        if node:
            next_node = node.next
            node.next = pre_node
            pre_node.pre = node
            if pre_node is self.head:
                pre_node.next = None
            if node is self.tail:
                node.pre = None
            return reverse(node, next_node)
        else:
            self.head = tail
            self.tail = pre_head

    return reverse(self.head, self.head.next)
```

![反转链表](http://img.blog.csdn.net/20151120150238050)

### 9. 清空链表
将头赋为空就好
```
"""清空链表"""
def clear(self):
    self.head.next = self.tail
    self.tail.pre = self.head
```
![清空链表](http://img.blog.csdn.net/20151120150303687)
---

git 路径 https://github.com/wangpanjun/datastructure.git

------

作者 [@小王]
2015 年 11月


