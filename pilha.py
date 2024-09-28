from base_structure import EstruturaEstatica


class Pilha(EstruturaEstatica):
    def __init__(self, capacidade, is_limited=None):
        super().__init__(capacidade)
        self.is_limited = is_limited = not is_limited is None

    def push(self, elem):
        if self.is_limited and self.is_full():
            raise ValueError("Pilha Cheia")

        self.adiciona(elem)
        print(self.adicionados, len(self.vetor))

    def top(self):
        if self.is_vazia():
            return None

        return self.vetor[self.adicionados - 1]

    def pop(self):
        if self.is_vazia():
            return None

        last = self.vetor[self.adicionados - 1]
        self.vetor[self.adicionados - 1] = None
        self.adicionados -= 1
        return last

    def is_full(self):
        return len(self.vetor) == self.adicionados

    def clear_recursive(self):
        if self.adicionados == 0:
            return

        self.vetor[self.adicionados - 1] = None
        self.adicionados -= 1
        self.clear_recursive()
