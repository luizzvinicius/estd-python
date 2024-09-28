from base_structure import EstruturaEstatica


class Pilha(EstruturaEstatica):
    def __init__(self, capacidade):
        super().__init__(capacidade)

    def empilha(self, elem):
        self.adiciona(elem)

    def topo(self):
        if self.is_vazia():
            return None

        return self.vetor[self.adicionados - 1]

    def desempilha(self):
        if self.is_vazia():
            return None

        last = self.vetor[self.adicionados - 1]
        self.vetor[self.adicionados - 1] = None
        self.adicionados -= 1
        return last
