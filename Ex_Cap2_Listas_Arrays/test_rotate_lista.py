import unittest
import time
from ods import ArrayDeque

class TestRotate(unittest.TestCase):
    def setUp(self):
        self.fila = ArrayDeque()
        self.fila.add_last(1)
        self.fila.add_last(2)
        self.fila.add_last(3)
        self.fila.add_last(4)
        self.tamanho = 1000000 # tamanho da lista a ser testada

        self.num_iter = 1000 # número de iterações para cada tamanho de lista
        # este número vai amortizar as várias execuções, fazendo o resultado ser mais confiável

        self.fator = 2 # fator admissível de diferença de tempos de execução

    def test_rotate_negativo(self):
        self.fila.rotate(-1)
        self.assertEqual(str(self.fila), '[2,3,4,1]', 'Erro: rotate(-1)')
        print("\nPassou no teste rotate negativo")

    def test_rotate_primeira_metade(self):
        self.fila.add_last(5)
        self.fila.rotate(2)
        self.assertEqual(str(self.fila), '[4,5,1,2,3]')
        print("\nPassou no teste rotate primeira metade")

    def test_rotate_segunda_metade(self):
        self.fila.add_last(5)
        self.fila.rotate(3)
        self.assertEqual(str(self.fila), '[3,4,5,1,2]')
        print("\nPassou no teste rotate segunda metade")

    def test_rotate_n(self):
        self.fila.add_last(5)
        self.fila.rotate(5)
        self.assertEqual(str(self.fila), '[1,2,3,4,5]')
        print("\nPassou no teste protate n")

    def test_rotate_multiplo_n(self):
        self.fila.add_last(5)
        self.fila.rotate(15)
        self.assertEqual(str(self.fila), '[1,2,3,4,5]')
        print("\nPassou no teste rotate mod n")

    def test_rotate_0(self):
        self.fila.add_last(5)
        self.fila.rotate(0)
        self.assertEqual(str(self.fila), '[1,2,3,4,5]')
        print("\nPassou no teste rotate 0 e mod n")

    def test_rotate_n_1(self):
        self.fila.add_last(5)
        self.fila.rotate(4)
        self.assertEqual(str(self.fila), '[2,3,4,5,1]')
        print("\nPassou no teste rotate n - 1")

    def test_rotate_n_2(self):
        self.fila.add_last(5)
        self.fila.rotate(6)
        self.assertEqual(str(self.fila), '[5,1,2,3,4]')
        print("\nPassou no teste rotate (n+1) mod n")

    def test_rotate_n_3(self):
        self.fila.add_last(5)
        self.fila.rotate(7)
        self.assertEqual(str(self.fila), '[4,5,1,2,3]')
        print("\nPassou no teste rotate (n+2) mod n")

    def test_rotate_sem_mover2(self):
        self.fila.rotate(2)
        self.assertEqual(str(self.fila.a), '[1 2 3 4]')
        self.assertEqual(self.fila.j, 2)
        print("\nPassou no teste rotate sem movimentar 2")

    def test_rotate_sem_mover3(self): 
        self.fila.rotate(3)
        self.assertEqual(str(self.fila.a), '[1 2 3 4]')
        self.assertEqual(self.fila.j, 1)
        print("\nPassou no teste rotate sem movimentar 3")

    def test_rotate_vazio(self):
        self.fila = ArrayDeque()
        self.fila.rotate(2)
        self.assertEqual(str(self.fila.a), '[None]')
        self.assertEqual(self.fila.j, 0)
        print("\nPassou no teste rotate lista vazia")

    def test_eficiencia1(self):
        '''Testa a eficiência do método rotate: O(1 + min(r, n-r))'''
        self.fila = ArrayDeque()
        for i in range(self.tamanho):
            self.fila.add_last(i)
        inicio = time.time()
        for _ in range(self.num_iter):
            self.fila.rotate(10)
        tempo1 = time.time() - inicio
        inicio = time.time()
        for _ in range(self.num_iter):
            self.fila.rotate(self.tamanho-10)
        tempo2 = time.time() - inicio
        print("\nTempo 1: ", tempo1, "Tempo 2: ", tempo2)
        self.assertLess(tempo2, self.fator*tempo1)
        self.assertLess(tempo1, self.fator*tempo2)
        print("\nPassou no teste de eficiência 1, O(1 + min(r, n-r))")

    def test_eficiencia2(self):
        '''Testa a eficiência do método rotate: O(1 + min(r, n-r))'''
        self.fila = ArrayDeque()
        for i in range(self.tamanho):
            self.fila.add_last(i)
        inicio = time.time()
        for _ in range(self.num_iter):
            self.fila.rotate(self.tamanho)
        tempo1 = time.time() - inicio
        inicio = time.time()
        for _ in range(self.num_iter):
            self.fila.rotate(0)
        tempo2 = time.time() - inicio
        print("\nTempo 1: ", tempo1, "Tempo 2: ", tempo2)
        self.assertLessEqual(tempo2, self.fator*tempo1)
        self.assertLessEqual(tempo1, self.fator*tempo2)
        print("\nPassou no teste de eficiência 2, O(1 + min(r, n-r))")

    def test_eficiencia3(self):
        '''Testa a eficiência do método rotate: O(1 + min(r, n-r))'''
        self.fila = ArrayDeque()
        for i in range(self.tamanho):
            self.fila.add_last(i)
        inicio = time.time()
        for _ in range(100):
            self.fila.rotate(100)
        tempo1 = time.time() - inicio
        inicio = time.time()
        for _ in range(100):
            self.fila.rotate(self.tamanho - 100)
        tempo2 = time.time() - inicio
        print("\nTempo 1: ", tempo1, "Tempo 2: ", tempo2)
        self.assertLess(tempo2, self.fator*tempo1)
        self.assertLess(tempo1, self.fator*tempo2)
        print("\nPassou no teste de eficiência 3, O(1 + min(r, n-r))")
        
if __name__ == '__main__':
    unittest.main()

