
class LinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def prepend(self, element):
        newNode = LinkedList(element)
        newNode.next = self
        return newNode

    def append(self, element):
        if self.next is None:
            self.next = LinkedList(element)
        else:
            self.next.append(element)
        return self

    def head(self):
        return self.data

    def tail(self):
        return self.next

    def contains(self, element):
        if self.data == element:
            return True
        elif self.next is None:
            return False
        else:
            return self.next.contains(element)

    def remove(self, element):
        if self.data == element:
            return self.next
        elif self.data is None or self.next is None:
            return self
        else:
            self.next = self.next.remove(element)
            return self

    def foreach(self, f):
        if self.data is not None:
            f(self.data)
            if self.next is not None:
                self.next.foreach(f)

    def map(self, f):
        if self.data is not None:
            ll = LinkedList(f(self.data))
            if self.next is not None:
                ll.next = self.next.map(f)
            return ll

    def __str__(self):
        return str(self.data) + ', ' + str(self.next)

