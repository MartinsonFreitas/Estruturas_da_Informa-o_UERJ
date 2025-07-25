'''
An array-based list implementation with O(1+min{i,n-i}) amortized update time.

Stores the list in an array, a, so that the i'th list item is stored
at a[(j+i)%len(a)].

Uses a doubling strategy for resizing a when it becomes full or too empty.
'''
from .utils import new_array
from .base import BaseList

class ArrayDeque(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = new_array(1)
        self.j = 0
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[(i+self.j)%len(self.a)]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[(i+self.j)%len(self.a)]
        self.a[(i+self.j)%len(self.a)] = x
        return y

    def add(self, i, x): 
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        if i < self.n/2:
            self.j = (self.j-1) % len(self.a)
            for k in range(i):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
        self.a[(self.j+i)%len(self.a)] = x
        self.n += 1

    def remove(self, i): 
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[(self.j+i)%len(self.a)]
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k-1)%len(self.a)]
            self.j = (self.j+1) % len(self.a)
        else:
            for k in range(i, self.n-1): 
                self.a[(self.j+k)%len(self.a)] = self.a[(self.j+k+1)%len(self.a)]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x
  
    def _resize(self):
        b = new_array(max(1, 2*self.n))
        for k in range(self.n):
            b[k] = self.a[(self.j+k)%len(self.a)]
        self.a = b
        self.j = 0
    
    def rotate(self, r):
        """Implemente um método rotate(r) que "gire" uma Lista para que o
        item de lista i se torne o item de lista (i + r) mod n. Quando
        executado em um ArrayDeque, rotate(r) deve ser executado
        em tempo O(1 + min{r, n − r}).
        """
        ### Apague o comando pass abaixo e escreva aqui sua solução,
        ### em seguida, execute o teste do diretorio superior
        ### com o comando
        ### python3 test_rotate_lista.py
        #pass
        
        if self.n == 0 or r == 0:
            return
        
        r = r % self.n
                                    
        # Caso especial quando o array está cheio - O(1) rotação
        #if self.n == len(self.a):
        #    self.j = (self.j + r) % len(self.a)           
        
        # Caso geral - O(min(r, n-r)) usando métodos existentes
        if r <= self.n - r:
            for _ in range(r):
                self.add_first(self.remove_last())                
        else:
            for _ in range(self.n - r):                    
                self.add_last(self.remove_first())
