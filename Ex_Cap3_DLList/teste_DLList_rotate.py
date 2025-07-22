from ods import DLList
import unittest
import time
from random import randint

class TesteRotate(unittest.TestCase):
    def setUp(self):
        self.lst = DLList([1, 2, 3, 4, 5])
        # Para teste de tempo de execução
        self.tamanhos = [1000, 10000, 100000, 1000000] # tamanho das listas a serem testadas
        # cada lista é 10 vezes maior que a anterior

        self.num_iter = 100 # número de iterações para cada tamanho de lista
        # este núemro vai amortizar as várias execuções, fazendo o resultado ser mais confiável

        self.fator = 2 # fator admissível de diferença de tempos de execução

    def test_rotate_1(self):
        # Testa rotação por 1
        self.lst.rotate(1)
        self.assertEqual(str(self.lst), "[5,1,2,3,4]")
        self.assertEqual(self.lst.size(), 5)
        self.assertEqual(self.lst.get(3), 3)

    def test_rotate_2(self):
        # Testa rotação por 2
        self.lst.rotate(2)
        self.assertEqual(str(self.lst), "[4,5,1,2,3]")
        self.assertEqual(self.lst.get(3), 2)

    def test_rotate_3(self):    
        # Testa rotação por 3
        self.lst.rotate(3)
        self.assertEqual(str(self.lst), "[3,4,5,1,2]")
        self.assertEqual(self.lst.get(3), 1)

    def test_rotate_5(self):
        # Testa rotação por 5
        self.lst.rotate(5)
        self.assertEqual(str(self.lst), "[1,2,3,4,5]")
        self.assertEqual(self.lst.get(3), 4)

    def test_rotate_7(self):
        # Testa rotação por 7 (equivalente a rotação por 2)
        self.lst.rotate(7)
        self.assertEqual(str(self.lst), "[4,5,1,2,3]")
        self.assertEqual(self.lst.get(3), 2)

    def test_rotate_0(self):
        # Testa rotação por 0 (sem rotação)
        self.lst.rotate(0)
        self.assertEqual(str(self.lst), "[1,2,3,4,5]")
        self.assertEqual(self.lst.get(3), 4)

    def test_rotate_grande(self):
        # Testa rotação por um número grande
        self.lst.rotate(102)
        self.assertEqual(str(self.lst), "[4,5,1,2,3]")
        self.assertEqual(self.lst.get(3), 2)

    def test_rotate_vazia(self):
        # Testa rotação de lista vazia
        lst_vazia = DLList()
        lst_vazia.rotate(2)
        self.assertEqual(str(lst_vazia), "[]")

    def test_rotate_3_em_10(self):
        dll = DLList()
        for i in range(10):
            dll.add_last(i)
        dll.rotate(3)
        for i in range(10):
            self.assertEqual(dll.get((i + 3) % 10), i)

    def test_rotate_1_get(self):
        dll = DLList()
        dll.add_first(1)
        dll.rotate(3)
        self.assertEqual(dll.size(), 1)
        self.assertEqual(str(dll), '[1]')

    def test_rotate_2b(self):
        dll = DLList()
        dll.add_last(1)
        dll.add_last(2)
        dll.rotate(3)
        self.assertEqual(dll.size(), 2)
        self.assertEqual(str(dll), '[2,1]')

    def test_rotate_3b(self):
        dll = DLList()
        dll.add_last(1)
        dll.add_last(2)
        dll.add_last(3)
        dll.rotate(3)
        self.assertEqual(dll.size(), 3)
        self.assertEqual(str(dll), "[1,2,3]")

    def test_rotate_4_insert(self):
        # Testa rotate com insert no meio da lista
        dll = DLList()
        dll.add_last(1)
        dll.add_last(2)
        dll.add_last(3)
        dll.add_last(4)
        dll.rotate(3)
        dll.add_last(5)
        dll.add_first(0)
        dll.add(2, 600)
        dll.add(4, 700)
        self.assertEqual(dll.size(), 8)
        self.assertEqual(str(dll), '[0,2,600,3,700,4,1,5]')

    def test_rotate_4_add_first_last(self):
        # Testa rotate com add_first e add_list na lista
        dll = DLList()
        dll.add_last(1)
        dll.add_last(2)
        dll.add_last(3)
        dll.add_last(4)
        dll.rotate(3)
        dll.add_last(5)
        dll.add_first(0)
        self.assertEqual(dll.size(), 6)
        self.assertEqual(str(dll), '[0,2,3,4,1,5]')

    def test_rotate_10(self):
        # Testa rotate com add_first e add_list na lista
        self.lst.rotate(3)
        self.lst.add_first(10)
        self.lst.add_last(20)
        self.lst.add_last(30)
        self.lst.add_last(40)
        self.lst.add_last(50)
        self.lst.rotate(3)
        self.assertEqual(self.lst.size(), 10)
        self.assertEqual(str(self.lst), '[30,40,50,10,3,4,5,1,2,20]')

    def test_complexidade_1(self):
        # Testa se os tempos de execução são semelhantes para operações
        # de rotação com o mesmo número de elementos, mas para
        # tamanhos diferentes de listas
        dll = DLList()
        tempos = []
        for n in self.tamanhos:
            for i in range(n):
                dll.add_last(i)
            t0 = time.time()
            for _ in range(self.num_iter):
                dll.rotate(3)
            t1 = time.time()
            tempos.append(t1 - t0)
        for i in range(1, len(tempos)):
            self.assertLessEqual(tempos[i], self.fator * tempos[i - 1])

    def test_complexidade_2(self):
        # Testa se os tempos de execução são semelhantes para operações
        # de rotação com o mesmo número de elementos, mas com rotações
        # no início e no final da lista
        dll = DLList()
        tempos = []
        tempos2 = []
        for n in self.tamanhos:
            for i in range(n):
                dll.add_last(i)
            t0 = time.time()
            for _ in range(self.num_iter):
                dll.rotate(3)
            t1 = time.time()
            tempos.append(t1 - t0)
            t3 = time.time()
            for _ in range(self.num_iter):
                dll.rotate(n - 3)
            t4 = time.time()
            tempos2.append(t4 - t3)
        for i in range(len(tempos)):
            self.assertLessEqual(tempos[i], self.fator * tempos2[i])
            
    def test_complexidade_3(self):
        # Testa se os tempos de execução são semelhantes para operações
        # com r pequeno e n grande. O tempo deve ser proporcional a r, independente de n
        dll = DLList()
        tempos = []
        for n in self.tamanhos:
            for i in range(n):
                dll.add_last(i)
            t0 = time.time()
            for _ in range(self.num_iter):
                dll.rotate(3)
            t1 = time.time()
            tempos.append(t1 - t0)
        for i in range(1, len(tempos)):
            self.assertLessEqual(tempos[i], self.fator * tempos[i - 1])

if __name__ == '__main__':
    unittest.main()