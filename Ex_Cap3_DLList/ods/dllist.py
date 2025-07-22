"""A doubly-linked list implementation with O(1+min{i, n-i}) update time"""
from .base import BaseList

class DLList(BaseList):

    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i):
        if i < self.n/2:
            p = self.dummy.next
            for _ in range(i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1):
                p = p.prev
        return p

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x

    def set(self, i, x): #@ReservedAssignment
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n:    raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

# Implemente o método rotate(r) que “rotaciona” uma DLList de modo que o 
# item i da lista se torne o item (i + r) mod n. Este método deve executar 
# em um tempo O(1 + min{r, n − r}) e não deve modificar nenhum nó na lista. 
# Você deve completá-lo sem alocar novos nós ou arrays temporários. 
# Tudo pode ser feitos apenas manipulando os valores de prev e next dos nós existentes.
    def rotate(self, r):
        
        if self.n <= 1 or r == 0:
            return

        r = r % self.n
        if r == 0:
            return

        # Encontra o ponto de quebra diretamente,
        # ou seja, o nó que se tornará o primeiro nó da nova lista.
        break_point = self.get_node(self.n - r)
        
        # Inverte a lista, ligando o último nó ao primeiro nó.
        last = self.dummy.prev
        first = self.dummy.next
        # 
        last.next = first
        first.prev = last
        # 
        # Atualiza o ponto de quebra...        
        self.dummy.next = break_point
        self.dummy.prev = break_point.prev
        #
        # O ponto de quebra agora é o primeiro elemento da nova lista.
        # Atualiza os ponteiros para o primeiro e o último nó.
        break_point.prev.next = self.dummy
        break_point.prev = self.dummy
        
        """
        Rotaciona a lista em r posições à esquerda (sentido horário).    
        Complexidade: O(1 + min{r, n-r})
        Exemplo: [1,2,3,4].rotate(1) -> [2,3,4,1]
        """