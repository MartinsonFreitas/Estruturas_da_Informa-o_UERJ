# Neste esboço de solução, optei por criar uma nova class e herdar tudo da classe ScapegoatTree.
# A classe ScapegoatTreeAlt é uma versão alternativa da ScapegoatTree que armazena e mantém
# explicitamente os tamanhos da subárvore com raiz em cada nó.
# Os testes dependem do atributo do nõ tam_sub_tree.
import math
from .utils import new_array
from .scapegoattree import ScapegoatTree
from .binarysearchtree import BinarySearchTree

def log32(q):
    return int(math.log(q, 1.5))

class ScapegoatTreeAlt(ScapegoatTree, BinarySearchTree):
    '''
    Implemente uma segunda versão da estrutura de dados 
    ScapegoatTree que armazena e mantém explicitamente os 
    tamanhos da subárvore com raiz em cada nó. 
    '''

    class Node(BinarySearchTree.Node):
        def __init__(self, x):
            super(ScapegoatTreeAlt.Node, self).__init__(x)
            # Aqui acrescentei o tamanho da subárvore. Os testes dependem desse atributo.
            self.tam_sub_tree = 1

        def update_sizeSTree(self):
            '''Atualiza o tamanho da subárvore com raiz em u. Implemente.'''
            pass
        
        def __str__(self):
            '''Retorna uma representação em string do nó. Modifiquei para ser compatível com os testes.'''
            return str(self.x) + ":" + str(self.tam_sub_tree)

    def _new_node(self, x):
        u = ScapegoatTreeAlt.Node(x)
        return u

    def __iter__(self):
        '''Retorna um iterador para os elementos armazenados na árvore, incluindo o tamanho armazenado no nó.'''
        u = self.first_node()
        while u != self.nil:
            yield u.x, u.tam_sub_tree
            u = self.next_node(u)

    
    def rebuild(self, u):
        '''Reconstrói a subárvore com raiz em u. Corrige bug do original.'''
        if u is self.nil: return
        ns = self._size(u)
        p = u.parent
        a = new_array(ns)
        self.pack_into_array(u, a, 0)
        if p == self.nil:
            self.r = self.build_balanced(a, 0, ns)
            self.r.parent = self.nil
        elif p.right == u:
            p.right = self.build_balanced(a, 0, ns)
            p.right.parent = p
        else:
            p.left = self.build_balanced(a, 0, ns)
            p.left.parent = p

    def add(self, x):
        '''
        Adiciona x à árvore. Retorna True se x foi adicionado e False caso contrário.
        O tamanho da sub-árvore vai mudar aqui. Implemente o código para manter o tamanho da subárvore.
        '''
        pass
    
    def remove(self, x):
        '''
        Remove x da árvore. Retorna True se x foi removido e False caso contrário.
        O tamanho da sub-árvore vai mudar aqui. Implemente o código para manter o tamanho da subárvore.
        '''
        pass
    
    def _update_sizeSTree(self, u):
        # Talvez esta função seja necessária para atualizar o tamanho da subárvore.
        pass

    def build_balanced(self, a, i, ns):
        # Talvez esta função tenha que ser modificada para funcionar com a nova info.
        if ns == 0:
            return self.nil
        m = ns // 2        
        a[i+m].left = self.build_balanced(a, i, m)
        if a[i+m].left != self.nil:
            a[i+m].left.parent = a[i+m]
        a[i+m].right = self.build_balanced(a, i+m+1, ns-m-1)
        if a[i+m].right != self.nil:
            a[i+m].right.parent = a[i+m]
        return a[i+m]