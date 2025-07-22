"""Algumas classes de base herdadas por outros módulos."""


class BaseCollection(object):
    """Classe de base para tudo."""

    def size(self):
        """Retorna o número de elementos do objeto."""
        return self.n

    def __len__(self):
        """Retorna o número de elementos do objeto."""
        return self.size()

    def __str__(self):
        """Retorna uma string com os elementos da estrutura."""
        return "[" + ",".join([str(x) for x in self]) + "]"

    def __repr__(self):
        """Retorna uma string com a representação da estrutura."""
        return (
            self.__class__.__name__
            + "(["
            + ",".join([repr(x) for x in self])
            + "])"
        )


class BaseSet(BaseCollection):
    """Classe de Base para todas as implementações de Set."""

    def add_all(self, a):
        """Adiciona elementos de a um a um na estrutura."""
        for x in a:
            self.add(x)

    def __in__(self, x):
        """Testa se elemento x está na estrutura."""
        return self.find(x) is not None

    def __eq__(self, a):
        """Testa se estrutura a é igual ao objeto."""
        if len(a) != len(self):
            return False
        for x in self:
            if x not in a:
                return False
        for x in a:
            if x not in self:
                return False
        return True

    def __ne__(self, a):
        """Testa se estrutura a é diferente do objeto."""
        return not self == a


class BaseList(BaseCollection):
    """Classe de Base para implementacões de lista."""

    def append(self, x):
        """Adiciona x ao final da lista."""
        self.add(self.size(), x)

    def add_all(self, iterable):
        for x in iterable:
            self.append(x)

    def clear(self):
        """This can be overridden with more efficient implementations."""
        while self.size() > 0:
            self.remove(self.size() - 1)

    def add_first(self, x):
        return self.add(0, x)

    def remove_first(self):
        return self.remove(0)

    def add_last(self, x):
        return self.add(self.size(), x)

    def remove_last(self):
        return self.remove(self.size() - 1)

    def insert(self, i, x):
        self.add(i, x)

    def __iter__(self):
        """This implementation is good enough for array-based lists."""
        for i in range(len(self)):
            yield (self.get(i))

    def __eq__(self, a):
        if len(a) != len(self):
            return False
        it1 = iter(a)
        it2 = iter(self)
        for i in range(len(a)):
            if it1.next() != it2.next():
                return False
        return True

    def __ne__(self, a):
        return not self == a

    def index(self, x):
        i = 0
        for y in self:
            if y == x:
                return i
            i += 1
        raise ValueError("%r is not in the list" % x)

    def remove_value(self, x):
        try:
            return self.remove(self.index(x))
        except ValueError:
            return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __delitem__(self, i):
        self.remove(i)
