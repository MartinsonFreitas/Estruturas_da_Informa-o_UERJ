from ods import Treap
import unittest
import random
import time

class TesteTreapGet(unittest.TestCase):

    def setUp(self):
        self.treap = Treap()
        self.fator = 2 # Fator de desempenho tolerado

    def test_get10(self):        
        for i in range(10):
            self.treap.add(i)
        for i in range(1,10):
            self.assertEqual(self.treap.get(i), i, "Elementos na ordem errada")

    def test_get10_inversa(self):
        for i in range(10):
            self.treap.add(9 - i)
        for i in range(10):
            self.assertEqual(self.treap.get(i), i, "Elementos invertidos na ordem errada")

    def test_get10_com_removido_central(self):
        for i in range(10):
            self.treap.add(i)
        self.treap.remove(5)
        for i in range(5):
            self.assertEqual(self.treap.get(i), i, "Elementos na ordem errada")
        for i in range(5,9):
            self.assertEqual(self.treap.get(i), i+1, "Elementos na ordem errada")

    def test_get100_com_removido_inicial(self):
        for i in range(100):
            self.treap.add(i)
        self.treap.remove(0)
        for i in range(99):
            self.assertEqual(self.treap.get(i), i+1, "Elementos na ordem errada")

    def test_get10_f(self):
        for i in range(10):
            self.treap.add(i+1)
        self.treap.add(0)
        for i in range(11):
            self.assertEqual(self.treap.get(i), i)

    def test_get10_g(self):
        for i in range(10):
            self.treap.add(i + 10)
        self.treap.add(0)
        for i in range(10):
            self.assertEqual(self.treap.get(i+1), i + 10)
        self.assertEqual(self.treap.get(0), 0)

    def test_get10_h(self):
        for i in range(10):
            self.treap.add(i)
        self.treap.remove(0)
        for i in range(9):
            self.assertEqual(self.treap.get(i), i+1)

    def test_get10_i(self):
        for i in range(1000):
            self.treap.add(random.randint(100, 1000000))
        for i in range(10):
            self.treap.add(i)
        for i in range(10):
            self.assertEqual(self.treap.get(i), i)

    def test_get10_j(self):
        for i in range(1000):
            while True:
                if self.treap.add(random.randint(0, 1000000)):
                    break
        for i in range(1000):
            self.treap.add(i+2000000)
        for i in range(1000):
            self.assertEqual(self.treap.get(i+1000), i+2000000)

    def test_vazio(self):
        self.assertEqual(self.treap.get(0), None)

    def test_um(self):
        self.treap.add(1)
        self.assertEqual(self.treap.get(0), 1)

    def test_dois(self):
        self.treap.add(1)
        self.treap.add(2)
        self.assertEqual(self.treap.get(0), 1)
        self.assertEqual(self.treap.get(1), 2)

    def test_dois_b(self):
        self.treap.add(2)
        self.treap.add(1)
        self.assertEqual(self.treap.get(0), 1)
        self.assertEqual(self.treap.get(1), 2)

    def test_complexidade_fim_meio(self):
        for i in range(100000):
            self.treap.add(i)
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(99999)
        t1 = time.time() - t_ini
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(1000)
        t2 = time.time() - t_ini
        self.assertLess(t1 , self.fator * t2, "Tem certeza que usou o tamanho da subávore?")
        self.assertLess(t2 , self.fator * t1, "Tem certeza que usou o tamanho da subávore?")

    def test_complexidade_fim_inicio(self):
        for i in range(100000):
            self.treap.add(i)
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(99999)
        t1 = time.time() - t_ini
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(5)
        t2 = time.time() - t_ini
        self.assertLess(t1 , self.fator * t2, "Tem certeza que usou o tamanho da subávore?")
        self.assertLess(t2 , self.fator * t1, "Tem certeza que usou o tamanho da subávore?")

    def test_complexidade_meio_inicio(self):
        for i in range(100000):
            self.treap.add(i)
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(50000)
        t1 = time.time() - t_ini
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(5)
        t2 = time.time() - t_ini
        self.assertLess(t1 , self.fator * t2, "Tem certeza que usou o tamanho da subávore?")
        self.assertLess(t2 , self.fator * t1, "Tem certeza que usou o tamanho da subávore?")

    def test_complexidade_inicio_random(self):
        for i in range(100000):
            self.treap.add(i)
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(0)
        t1 = time.time() - t_ini
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(random.randint(0, 100000))
        t2 = time.time() - t_ini
        self.assertLess(t1 , self.fator * t2, "Tem certeza que usou o tamanho da subávore?")
        self.assertLess(t2 , self.fator * t1, "Tem certeza que usou o tamanho da subávore?")

    def test_complexidade_fim_random(self):
        for i in range(100000):
            self.treap.add(i)
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(99999)
        t1 = time.time() - t_ini
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(random.randint(0, 1000))
        t2 = time.time() - t_ini
        self.assertLess(t1 , self.fator * t2, "Tem certeza que usou o tamanho da subávore?")
        self.assertLess(t2 , self.fator * t1, "Tem certeza que usou o tamanho da subávore?")

    def test_complexidade_meio_random(self):
        for i in range(100000):
            self.treap.add(i)
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(50000)
        t1 = time.time() - t_ini
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(random.randint(0, 1000))
        t2 = time.time() - t_ini
        self.assertLess(t1 , self.fator * t2, "Tem certeza que usou o tamanho da subávore?")
        self.assertLess(t2 , self.fator * t1, "Tem certeza que usou o tamanho da subávore?")

    def test_complexidade_random_random(self):
        for i in range(100000):
            self.treap.add(i)
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(random.randint(0, 10000))
        t1 = time.time() - t_ini
        t_ini = time.time()
        for _ in range (10):
            self.treap.get(random.randint(90000, 100000))
        t2 = time.time() - t_ini
        self.assertLess(t1 , self.fator * t2, "Tem certeza que usou o tamanho da subávore?")
        self.assertLess(t2 , self.fator * t1, "Tem certeza que usou o tamanho da subávore?")


if __name__ == '__main__':
    unittest.main()
