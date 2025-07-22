import random

class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.size = 1
        self.left = None
        self.right = None

def size(node):
    return node.size if node else 0

def update_size(node):
    if node:
        node.size = size(node.left) + size(node.right) + 1

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update_size(y)
    update_size(x)
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    update_size(x)
    update_size(y)
    return y

def insert(root, key, priority):
    if not root:
        return Node(key, priority)

    if key < root.key:
        root.left = insert(root.left, key, priority)
        if root.left.priority > root.priority:
            root = rotate_right(root)
    else:
        root.right = insert(root.right, key, priority)
        if root.right.priority > root.priority:
            root = rotate_left(root)

    update_size(root)
    return root

def get(root, i):
    if not root:
        return None

    left_size = size(root.left)
    if i == left_size:
        return root.key
    elif i < left_size:
        return get(root.left, i)
    else:
        return get(root.right, i - left_size - 1)

# Exemplo de uso
treap = None

# Inserindo chaves na Treap com prioridades aleatórias
keys = [3, 1, 4, 6, 9, 2, 5, 7]
for key in keys:
    priority = random.random()
    treap = insert(treap, key, priority)

# Obtendo a chave na posição 2 (índice 1)
result = get(treap, 1)
print("Chave na posição 2:", result)
