import unittest
from ods import ScapegoatTreeAlt

class TesteScapegoatTree_alternativa(unittest.TestCase):
    def setUp(self):
        self.st = ScapegoatTreeAlt()
        # Árvore do livro
        self.st.add(7)
        self.st.add(6)
        self.st.add(8)
        self.st.add(5)
        self.st.add(9)
        self.st.add(2)
        self.st.add(1)
        self.st.add(4)
        self.st.add(0)
        self.st.add(3)

    def test_arvore_inicial(self):
        print("\nÁrvore inicial: ", self.st)
        self.assertEqual(str(self.st), "[(0, 1),(1, 2),(2, 5),(3, 1),(4, 2),(5, 6),(6, 7),(7, 10),(8, 2),(9, 1)]")        

    def test_insere_1(self):        
        print("\nInserindo um elemento\nAntes: ", self.st)
        self.st.add(3.5)
        print("Depois: ", self.st)
        self.assertEqual(str(self.st), "[(0, 1),(1, 3),(2, 1),(3, 7),(3.5, 1),(4, 3),(5, 1),(6, 8),(7, 11),(8, 2),(9, 1)]")

    def test_isere_2(self):
        print("\nInserindo dois elementos\nAntes: ", self.st)
        self.st.add(3.5)
        self.st.add(3.2)
        print("Depois: ", self.st)
        self.assertEqual(str(self.st), 
                         "[(0, 1),(1, 3),(2, 1),(3, 8),(3.2, 1),(3.5, 2),(4, 4),(5, 1),(6, 9),(7, 12),(8, 2),(9, 1)]")

    def test_remove_1(self):
        print("\nRemovendo um elemento\nAntes: ", self.st)
        self.st.remove(3)
        print("Depois: ", self.st)
        self.assertEqual(str(self.st), "[(0, 1),(1, 2),(2, 4),(4, 1),(5, 5),(6, 6),(7, 9),(8, 2),(9, 1)]")

    def test_remove_2(self):
        print("\nRemovendo dois elementos\nAntes: ", self.st)
        self.st.remove(3)
        self.st.remove(4)
        print("Depois: ", self.st)
        self.assertEqual(str(self.st), "[(0, 1),(1, 2),(2, 3),(5, 4),(6, 5),(7, 8),(8, 2),(9, 1)]")

    def test_remove_muitos(self):
        print("\nRemovendo muitos elementos\nAntes: ", self.st)
        self.st.remove(3)
        self.st.remove(4)
        self.st.remove(9)
        self.st.remove(8)
        self.st.remove(0)
        self.st.remove(1)
        print("Depois: ", self.st)
        self.assertEqual(str(self.st), "[(2, 1),(5, 2),(6, 4),(7, 1)]")

    def test_remove_todos(self):
        print("\nRemovendo todos os elementos.\nAntes: ", self.st)
        self.st.remove(3)
        self.st.remove(4)
        self.st.remove(9)
        self.st.remove(8)
        self.st.remove(0)
        self.st.remove(1)
        self.st.remove(2)
        self.st.remove(5)
        self.st.remove(6)
        self.st.remove(7)
        print("Depois: ", self.st)
        self.assertEqual(str(self.st), "[]")

    def test_find(self):
        print("\nBuscando um elemento\nAntes: ", self.st)
        self.assertEqual(self.st.find(3), 3)
        print("Depois: ", self.st)  

    def test_find_vazio(self):
        print("\nBuscando um elemento em uma árvore vazia")
        st = ScapegoatTreeAlt()
        self.assertEqual(st.find(10), None)

    def test_tamanho_arvore(self):
        print("\nTeste tamanho da árvore")
        self.st.add(3.5)
        self.assertEqual(self.st.size(), 11)

if __name__ == '__main__':
    unittest.main()