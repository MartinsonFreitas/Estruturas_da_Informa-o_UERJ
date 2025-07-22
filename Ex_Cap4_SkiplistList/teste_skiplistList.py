from ods import SkiplistList
import unittest
import time

class Teste_trucate(unittest.TestCase):
    def setUp(self):
        self.skl = SkiplistList()
        self.skl.add(0, 1)
        self.skl.add(1, 2)
        self.skl.add(2, 3)
        self.skl.add(3, 4)
        self.skl.add(4, 5)
        self.skl.add(5, 6)
        self.skl.add(6, 7)
        self.skl.add(7, 8)
        self.skl.add(8, 9)
        self.skl.add(9, 10)
        self.tam_teste = 10000
        self.fator = 3 # fator admissível de diferença de tempos de execução

    def test_truncate_00(self):
        new_skl = self.skl.truncate(0)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 0)
        self.assertEqual(new_skl.n, 10)
        self.assertEqual(new_skl.get(0), 1)
        self.assertEqual(new_skl.get(9), 10)

    def test_truncate_01(self):
        new_skl = self.skl.truncate(1)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 1)
        self.assertEqual(new_skl.n, 9)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(new_skl.get(0), 2)
        self.assertEqual(new_skl.get(8), 10)

    def test_truncate_02(self):
        new_skl = self.skl.truncate(2)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 2)
        self.assertEqual(new_skl.n, 8)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(1), 2)
        self.assertEqual(new_skl.get(0), 3)
        self.assertEqual(new_skl.get(7), 10)

    def test_truncate_03(self):
        new_skl = self.skl.truncate(3)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 3)
        self.assertEqual(new_skl.n, 7)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(2), 3)
        self.assertEqual(new_skl.get(0), 4)
        self.assertEqual(new_skl.get(6), 10)

    def test_truncate_04(self):
        new_skl = self.skl.truncate(4)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 4)
        self.assertEqual(new_skl.n, 6)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(3), 4)
        self.assertEqual(new_skl.get(0), 5)
        self.assertEqual(new_skl.get(5), 10)

    def test_truncate_05(self):
        new_skl = self.skl.truncate(5)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 5)
        self.assertEqual(new_skl.n, 5)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(4), 5)
        self.assertEqual(new_skl.get(0), 6)
        self.assertEqual(new_skl.get(4), 10)

    def test_truncate_06(self):
        new_skl = self.skl.truncate(6)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 6)
        self.assertEqual(new_skl.n, 4)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(5), 6)
        self.assertEqual(new_skl.get(0), 7)
        self.assertEqual(new_skl.get(3), 10)

    def test_truncate_07(self):
        new_skl = self.skl.truncate(7)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 7)
        self.assertEqual(new_skl.n, 3)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(6), 7)
        self.assertEqual(new_skl.get(0), 8)
        self.assertEqual(new_skl.get(2), 10)

    def test_truncate_08(self):
        new_skl = self.skl.truncate(8)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 8)
        self.assertEqual(new_skl.n, 2)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(7), 8)
        self.assertEqual(new_skl.get(0), 9)
        self.assertEqual(new_skl.get(1), 10)

    def test_truncate_09(self):
        new_skl = self.skl.truncate(9)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 9)
        self.assertEqual(new_skl.n, 1)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(8), 9)
        self.assertEqual(new_skl.get(0), 10)

    def test_truncate_10(self):
        new_skl = self.skl.truncate(10)
        print("Nova skiplist", new_skl)
        print("Skiplist original", self.skl)
        self.assertEqual(self.skl.n, 10)
        self.assertEqual(new_skl.n, 0)
        self.assertEqual(self.skl.get(0), 1)
        self.assertEqual(self.skl.get(9), 10)
        
    def test_truncate_11(self):
        aux_skl = SkiplistList()
        for i in range(1000):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(10)
        self.assertEqual(aux_skl.n, 10)
        self.assertEqual(new_skl.n, 990)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(9), 9)
        self.assertEqual(new_skl.get(0), 10)
        self.assertEqual(new_skl.get(989), 999)
        
    def test_truncate_12(self):
        aux_skl = SkiplistList()
        for i in range(1000):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(990)
        self.assertEqual(aux_skl.n, 990)
        self.assertEqual(new_skl.n, 10)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(989), 989)
        self.assertEqual(new_skl.get(0), 990)
        self.assertEqual(new_skl.get(9), 999)

    def test_truncate_13(self):
        aux_skl = SkiplistList()
        for i in range(1000):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(1000)
        self.assertEqual(aux_skl.n, 1000)
        self.assertEqual(new_skl.n, 0)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(999), 999)

    def test_truncate_14(self):
        aux_skl = SkiplistList()
        for i in range(1000):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(500)
        self.assertEqual(aux_skl.n, 500)
        self.assertEqual(new_skl.n, 500)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(499), 499)
        self.assertEqual(new_skl.get(0), 500)
        self.assertEqual(new_skl.get(499), 999)

    # lista grande, truncando em 100
    def test_truncate_15(self):
        aux_skl = SkiplistList()
        for i in range(10*self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        self.assertEqual(aux_skl.n, 100)
        self.assertEqual(new_skl.n, 99900)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(99), 99)
        self.assertEqual(new_skl.get(0), 100)
        self.assertEqual(new_skl.get(99899), 99999)

    # lista grande, truncando em 99900
    def test_truncate_16(self):
        aux_skl = SkiplistList()
        for i in range(10*self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(99900)
        self.assertEqual(aux_skl.n, 99900)
        self.assertEqual(new_skl.n, 100)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(99899), 99899)
        self.assertEqual(new_skl.get(0), 99900)
        self.assertEqual(new_skl.get(99), 99999)

    # lista grande, truncando depois do final
    def test_truncate_17(self):
        aux_skl = SkiplistList()
        for i in range(10*self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100000)
        self.assertEqual(aux_skl.n, 100000)
        self.assertEqual(new_skl.n, 0)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(99999), 99999)

    # lista grande, truncando no meio
    def test_truncate_18(self):
        aux_skl = SkiplistList()
        for i in range(10*self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(50000)
        self.assertEqual(aux_skl.n, 50000)
        self.assertEqual(new_skl.n, 50000)
        self.assertEqual(aux_skl.get(0), 0)
        self.assertEqual(aux_skl.get(49999), 49999)
        self.assertEqual(new_skl.get(0), 50000)
        self.assertEqual(new_skl.get(49999), 99999)

    # lista grande, truncando em 100 e adicionando no início da lista original
    def test_truncate_19(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        aux_skl.add(0, 100)
        self.assertEqual(aux_skl.get(0), 100)
        self.assertEqual(aux_skl.get(100), 99)

    # lista grande, truncando em 100 e adicionando no início da lista nova
    def test_truncate_20(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        new_skl.add(0, 200)
        self.assertEqual(new_skl.get(0), 200)
        self.assertEqual(new_skl.get(self.tam_teste-100), self.tam_teste-1)

    # lista grande, truncando em 100 e adicionando no final da lista original
    def test_truncate_21(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        aux_skl.add(100, 100)
        self.assertEqual(aux_skl.get(99), 99)
        self.assertEqual(aux_skl.get(100), 100)

    # lista grande, truncando em 100 e adicionando no final da lista nova
    def test_truncate_22(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        new_skl.add(self.tam_teste-100, 200)
        self.assertEqual(new_skl.get(self.tam_teste-100), 200)

    # lista grande, truncando em 100 e adicionando no meio da lista original
    def test_truncate_23(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        aux_skl.add(50, 100)
        self.assertEqual(aux_skl.get(50), 100)
        self.assertEqual(aux_skl.get(100), 99)

    # lista grande, truncando em 100 e adicionando no meio da lista nova
    def test_truncate_24(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        new_skl.add(50, 200)
        self.assertEqual(new_skl.get(50), 200)
        self.assertEqual(new_skl.get(self.tam_teste-100), self.tam_teste-1)

    # lista grande, truncando em 100 e retirando do meio da lista original
    def test_truncate_25(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        aux_skl.truncate(100)
        aux_skl.remove(50)
        self.assertEqual(aux_skl.get(50), 51)
        self.assertEqual(aux_skl.get(98), 99)

    # lista grande, truncando em 100 e retirando do meio da lista nova
    def test_truncate_26(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        new_skl = aux_skl.truncate(100)
        new_skl.remove(50)
        self.assertEqual(new_skl.get(50), 151)
        self.assertEqual(new_skl.get(self.tam_teste-100-2), self.tam_teste-1)

    # lista grande, truncando em 100 e retirando do início da lista original
    def test_truncate_27(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        aux_skl.truncate(100)
        aux_skl.remove(0)
        self.assertEqual(aux_skl.get(0), 1)
        self.assertEqual(aux_skl.get(98), 99)

    def test_eficiencia01(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        start = time.time()
        new_skl = aux_skl.truncate(100)
        end = time.time()
        tempo1 = end - start
        print("Tempo de execução 1: ", tempo1)
        aux_skl2 = SkiplistList()
        for i in range(10 * self.tam_teste):
            aux_skl2.add(i, i)
        start = time.time()
        new_skl2 = aux_skl2.truncate(100)
        end = time.time()
        tempo2 = end - start
        if tempo1 == 0:
            tempo1 = 0.000001  # Valor mínimo para evitar divisão por zero
        print("Tempo de execução 2: ", tempo2, "relação: ", tempo2/tempo1)
        self.assertLess(tempo2, self.fator*tempo1)

    def test_eficiencia02(self):
        aux_skl = SkiplistList()
        for i in range(self.tam_teste):
            aux_skl.add(i, i)
        start = time.time()
        new_skl = aux_skl.truncate(self.tam_teste-100)
        end = time.time()
        tempo1 = end - start
        print("Tempo de execução 1: ", tempo1)
        aux_skl2 = SkiplistList()
        for i in range(10*self.tam_teste):
            aux_skl2.add(i, i)
        start = time.time()
        new_skl2 = aux_skl2.truncate(10*self.tam_teste-100)
        end = time.time()
        tempo2 = end - start
        if tempo1 == 0:
            tempo1 = 0.000001  # Valor mínimo para evitar divisão por zero
        print("Tempo de execução 2: ", tempo2, "relação: ", tempo2/tempo1)
        self.assertLess(tempo2, self.fator*tempo1)

if __name__ == "__main__":
    unittest.main()