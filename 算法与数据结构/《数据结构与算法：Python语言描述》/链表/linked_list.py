class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:
    """
    单链表
    高效的首端加入/删除
    低效的尾端加入/删除
    """
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("empty LList")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("empty LList")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def __iter__(self):
        def iterator():
            p = self._head
            while p is not None:
                yield p.elem
                p = p.next
        return iterator()

    def __str__(self):
        return " -> ".join(str(i) for i in self)


class LList1(LList):
    """
    带尾节点引用的单链表
    高效的首端加入/删除，尾端加入
    低效的尾端删除
    """
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("empty LList1")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


class LCList:
    """
    指向尾节点的循环单链表
    高效的首端加入/删除，尾端加入
    低效的尾端删除
    """
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        if self._rear is None:
            p = LNode(elem)
            p.next = p
            self._rear = p
        else:
            self._rear.next = LNode(elem, self._rear.next)

    def append(self, elem):
        if self._rear is None:
            p = LNode(elem)
            p.next = p
            self._rear = p
        else:
            self._rear.next = LNode(elem, self._rear.next)
            self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("empty LCList")
        if self._rear.next is self._rear:
            e = self._rear.elem
            self._rear = None
            return e
        e = self._rear.next.elem
        self._rear.next = self._rear.next.next
        return e

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow("empty LCList")
        if self._rear.next is self._rear:
            e = self._rear.elem
            self._rear = None
            return e
        p = self._rear
        while p.next is not self._rear:
            p = p.next
        e = self._rear.elem
        self._rear = p
        return e

    def __iter__(self):
        def iterator():
            p = self._rear
            if p is None:
                return
            while p.next is not self._rear:
                yield p.next.elem
                p = p.next
            yield self._rear.elem
        return iterator()


class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


class DLList(LList1):
    """
    带尾节点引用的双链表
    高效的首端加入/删除，尾端加入/删除
    """
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            p = DLNode(elem, None, self._head)
            self._head.prev = p
            self._head = p

    def append(self, elem):
        if self._head is None:
            self._head = DLNode(elem)
            self._rear = self._head
        else:
            p = DLNode(elem, self._rear, None)
            self._rear.next = p
            self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("empty DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("empty DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e


class DLCList:
    """
    指向首节点的循环双链表
    """
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        if self._head is None:
            p = DLNode(elem)
            p.next = p
            p.prev = p
            self._head = p
        else:
            p = DLNode(elem, self._head.prev, self._head)
            self._head.prev.next = p
            self._head.prev = p
            self._head = p

    def append(self, elem):
        if self._head is None:
            p = DLNode(elem)
            p.next = p
            p.prev = p
            self._head = p
        else:
            p = DLNode(elem, self._head.prev, self._head)
            self._head.prev.next = p
            self._head.prev = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("empty DLCList")
        if self._head.next is self._head:
            


if __name__ == "__main__":
    a = DLList()
    for i in range(10):
        a.prepend(i)
    for i in range(10, 20):
        a.append(i)
    for i in a:
        print(i)
