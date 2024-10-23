class Membro:
    def __init__(self, nome, email, proximo=None):
        self.nome = nome
        self.email = email
        self.proximo = proximo

    def get_membro(self):
        return self.nome

    def set_membro(self, nome, email):
        self.nome = nome
        self.email = email

    def get_proximo(self):
        return self.proximo

    def set_proximo(self, proximo):
        self.proximo = proximo

    def to_string(self):
        return f"(nome={self.nome}, email={self.email})"


class CircularLinkedList:
    def __init__(self):
        self.inicio = None
        self.ultimo = self.inicio
        self.tamanho = 0
        self.proximo_membro = self.inicio

    def adicionar_membro(self, membro):
        if self.tamanho == 0:
            self.inicio = membro
        else:
            self.ultimo.set_proximo(membro)
        self.proximo_membro = self.inicio
        self.ultimo = membro
        self.ultimo.set_proximo(self.inicio)
        self.tamanho += 1

    def remover_membro(self, nome):
        if self.tamanho == 0:
            raise RuntimeError("Lista está vazia")

        index = self._index(nome)
        if index == -1:
            raise RuntimeError("Elemento não encontrado")

        if index == 0:
            self._remove_inicio()
        elif index == self.tamanho - 1:
            self._remove_ultimo()
        else:
            atual = self.inicio
            removido = None
            for _ in range(self.tamanho - 1):
                no_removido = atual.get_proximo()
                proximo_no = atual.get_proximo().get_proximo()
                if nome == no_removido.get_membro():
                    removido = nome
                    atual.set_proximo(proximo_no)
                    no_removido.set_membro(None, None)
                    no_removido.set_proximo(None)
                    self.tamanho -= 1
                atual = atual.get_proximo()
            return removido

    def _index(self, elem):
        inicial = self.inicio
        for i in range(self.tamanho):
            if inicial.get_membro() == elem:
                return i
            inicial = inicial.get_proximo()
        return -1

    def _remove_inicio(self):
        atual = self.inicio
        removido = atual.get_membro()
        self.inicio = self.inicio.get_proximo()
        atual.set_membro(None, None)
        atual.set_proximo(None)
        self.tamanho -= 1
        return removido

    def _remove_ultimo(self):
        penultimo_no = self.inicio
        for _ in range(self.tamanho - 2):
            penultimo_no = penultimo_no.get_proximo()

        removido = self.ultimo.get_membro()
        self.ultimo.set_membro(None, None)
        self.ultimo = penultimo_no
        penultimo_no.set_proximo(None)
        self.ultimo.set_proximo(self.inicio)
        self.tamanho -= 1
        return removido

    def proximo_responsavel(self):
        self.proximo_membro = self.proximo_membro.get_proximo()
        return self.proximo_membro

    def __len__(self):
        return self.tamanho

    def __str__(self):
        if self.tamanho == 0:
            return "[]"

        s = "["
        atual = self.inicio
        for _ in range(self.tamanho - 1):
            s += f"{atual.to_string()}, "
            atual = atual.get_proximo()

        s += f"{atual.to_string()}]"
        return s


lista = CircularLinkedList()

lista.adicionar_membro(Membro("luiz1", "luiz1@"))
lista.adicionar_membro(Membro("luiz2", "luiz2@"))
lista.adicionar_membro(Membro("luiz3", "luiz3@"))
lista.adicionar_membro(Membro("luiz4", "luiz4@"))
lista.adicionar_membro(Membro("luiz5", "luiz5@"))

print(lista.proximo_responsavel().to_string())
print(lista.proximo_responsavel().to_string())
lista.remover_membro("luiz4")
print(lista.proximo_responsavel().to_string())
print(lista.proximo_responsavel().to_string())
print(lista.proximo_responsavel().to_string())
print(lista.proximo_responsavel().to_string())
print(lista.proximo_responsavel().to_string())
print(lista.proximo_responsavel().to_string())
print(lista.proximo_responsavel().to_string())

print(lista)
