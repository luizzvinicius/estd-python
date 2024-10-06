class EmptyQueue(Exception):
    def __init__(self, mensagem="Fila está vazia"):
        super().__init__(mensagem)


class ElementNotFound(Exception):
    def __init__(self, mensagem="Element not found"):
        super().__init__(mensagem)


class SetWithQueue:
    def __init__(self, capacidade = None):
        capacidade = 16 if capacidade is None else capacidade
        self.lista = [None] * capacidade
        self.adicionados = 0
        # self._inicio = 0

    def size(self):
        return self.adicionados

    def is_empty(self):
        return self.adicionados == 0

    def is_full(self):
        return self.adicionados == len(self.lista)

    def add(self, element):
        if self.contains(element):
            return

        self._aumenta_capacidade()
        self.lista[self.adicionados] = element
        self.adicionados += 1

    def remove(self, element):
        if self.is_empty():
            raise EmptyQueue()

        index = self.index_of(element)
        if index == -1:
            raise ValueError("Element not found")

        excluded = self.lista[index]

        for i in range(index, self.adicionados):
            self.lista[i] = self.lista[i + 1]

        self.adicionados -= 1
        return excluded

    def index_of(self, element):
        for index, v in enumerate(self.lista):
            if v == element:
                return index
        return -1

    def contains(self, element):
        for e in self.lista:
            if e == element:
                return True
        return False

    def list(self):
        if self.is_empty():
            return "[]"

        s = "["
        for e in self.lista:  # tirar o if
            if e is None:
                break
            s += f"{str(e)}, "

        return f"{s[:-2]}]"
        

    def _aumenta_capacidade(self):
        if self.is_full():
            new_list = [None] * len(self.lista) * 2

            for i, element in enumerate(self.lista):
                new_list[i] = element

            self.lista = new_list


lista = SetWithQueue(2)
lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)
lista.remove(2)

print(lista.contains(3))
print(lista.list(), lista.size())
