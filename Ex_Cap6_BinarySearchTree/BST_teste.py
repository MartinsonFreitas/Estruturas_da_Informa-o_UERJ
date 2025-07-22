from ods import *
import random
import unittest
import time


def gerar_numeros(k, minimo, maximo):
  """
  Gera uma lista de k números aleatórios dentro de um intervalo especificado.

  Args:
    k: O número de elementos na lista.
    minimo: O valor mínimo do intervalo (inclusivo).
    maximo: O valor máximo do intervalo (inclusivo).

  Returns:
    Uma lista de k números aleatórios.
"""
  lista_aleatoria = []
  for _ in range(k):
    numero_aleatorio = random.randint(minimo, maximo)
    lista_aleatoria.append(numero_aleatorio)
  return lista_aleatoria

def gerar_arvore(tamanho, minimo, maximo):
    """
    Gera uma árvore de busca binária com elementos aleatórios.

    Args:
        tamanho: O número de elementos na árvore.
        minimo: O valor mínimo do intervalo (inclusivo).
        maximo: O valor máximo do intervalo (inclusivo).

    Returns:
        Uma instância de BinarySearchTree com elementos aleatórios.
    """
    bst = BinarySearchTree()
    elementos = gerar_numeros(tamanho, minimo, maximo)
    for elemento in elementos:
        bst.add(elemento)
    return bst

class TesteBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()    

    def teste(self):
        """Teste para verificar se o método obtemMouI funciona corretamente."""
        # Adicionar elementos à árvore
        elementos = [10, 20, 30, 40, 50]
        for elemento in elementos:
            self.bst.add(elemento)
        
        # Testar o método obtemMouI
        x = 25
        resultado = self.bst.obtemMouI(x)
        
        # Verificar se os resultados estão corretos
        assert resultado == [20, 10], f"Erro: esperado [20, 10], mas obteve {resultado}"
        print("Teste passou com sucesso!")
        
    def testes_aleatorios(self):      
    # Gerar números aleatórios para adicionar à árvore
      print("\nGerando uma lista aleatória de números...")
      # Definir o tamanho da lista e o intervalo de valores
      tamanho = 30
      minimo = 1
      maximo = 100
      elementos = gerar_numeros(tamanho, minimo, maximo)
      print(f"Lista aleatória gerada: {elementos} \n")
      
      '''
      # Adicionar elementos à árvore
      elements = [ 3, 2, 8, 10, 21, 1, 6, 9, 12]
      
      for element in elementos:
          bst.add(element)
      '''
      arvore = gerar_arvore(tamanho, minimo, maximo)
      # Imprimir a árvore em ordem
      print("Árvore em ordem:")
      for item in arvore:
        print(item, end=" ")
      print("\n")
      
      '''
      # Testar o método first_node
      first_node = bst.first_node()
      print(f"Primeiro nó da árvore: {first_node.x if first_node != bst.nil else 'Árvore vazia'}")
      # Testar o método next_node
      next_node = bst.next_node(first_node)
      print(f"Próximo nó após o primeiro: {next_node.x if next_node != bst.nil else 'Não há próximo nó'}\n")
      '''
      
      # testar o método size
      size = arvore.size()
      print(f"Tamanho da árvore: {size}")
      # Testar o método height
      height = arvore.height()
      print(f"Altura da árvore: {height}\n")   
          
      # Testar o método obtemMouI
      x_value = random.randint(minimo, maximo)
      result = arvore.obtemMouI(x_value)

      # Imprimir elementos menores ou iguais a x
      print(f"Elementos menores ou iguais a {x_value}:")
      print(result)
      print("\n")


if __name__ == "__main__":         
  unittest.main()