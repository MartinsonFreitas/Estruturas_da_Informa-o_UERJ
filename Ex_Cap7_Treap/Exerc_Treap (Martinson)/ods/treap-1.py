import random

from .binarysearchtree import BinarySearchTree

class Treap(BinarySearchTree):
    class Node(BinarySearchTree.Node):
        def __init__(self, x):
            super(Treap.Node, self).__init__(x)
            self.p = random.random()
            
        def __str__(self):
            return "[%r,%f]" % (self.x, self.p)

    def __init__(self, iterable=[]):
        self.nil = Treap.Node(None)
        self.nil.size = 0
        self.nil.left = self.nil.right = self.nil
        self.r = self.nil
        for x in iterable:
            self.add(x)

    def _size(self, u):
        return 0 if u == self.nil else u.size

    def _update_size(self, u):
        u.size = self._size(u.left) + self._size(u.right) + 1

   
    def _new_node(self, x):
        return Treap.Node(x)
        
    def add(self, x):
        u = self._new_node(x)
        if self.add_node(u):
            self.bubble_up(u)
            return True
        return False

    def remove(self, x):
        u = self._find_last(x)
        if u is not None and u.x == x:
            self.trickle_down(u)
            self.splice(u)
            return True
        return False
        
    
    def trickle_down(self, u):
        while u.left is not None or u.right is not None:
            if u.left is None:
                self.rotate_left(u)
            elif u.right is None:
                self.rotate_right(u)
            elif u.left.p < u.right.p:
                self.rotate_right(u)
            else:
                self.rotate_left(u)
            if self.r == u:
                self.r = u.parent

    def add_node(self, u):
        if super(Treap, self).add_node(u):
            self._update_size(u)
            return True
        return False

    def _rotate_left(self, u):
        super(Treap, self)._rotate_left(u)
        self._update_size(u)
        self._update_size(u.parent)

    def _rotate_right(self, u):
        super(Treap, self)._rotate_right(u)
        self._update_size(u)
        self._update_size(u.parent)
            
    def bubble_up(self, u):
        while u != self.r and u.parent.p > u.p:
            if u.parent.right == u:
                self.rotate_left(u.parent)
            else:
                self.rotate_right(u.parent)

        if u.parent == self.nil:
            self.r = u

    def get(self, i):
        return self._get_recursive(self.r, i)

    def _get_recursive(self, u, i):
        if u is None:
            return None

        left_size = self._size(u.left)
        
        if i == left_size:
            return u.x
        elif i < left_size:
            return self._get_recursive(u.left, i)
        else:
            return self._get_recursive(u.right, i - left_size - 1)
        