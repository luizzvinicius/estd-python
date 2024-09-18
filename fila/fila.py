from base.base_structure import EstruturaEstatica


class Fila(EstruturaEstatica):
    def __init__(self, capacidade):
        super().__init__(capacidade)

    def enfileira(self, elem):
        self.adiciona(elem)

    def espiar(self):
        if self.is_vazia():
            return None

        return self.vetor[0]

    def desenfileira(self):
        if self.is_vazia():
            return None

        first = self.vetor[0]
        self.remove(0)
        return first
