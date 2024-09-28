from base_structure import EstruturaEstatica


class Vetor(EstruturaEstatica):
    def __init__(self, capacidade):
        super().__init__(capacidade)

    def adiciona(self, elem, index=None):
        if index is None:
            super().adiciona(elem)
        else:
            super().adiciona(elem, index)

    def busca(self, elem):
        """Retorna índice"""
        for i, v in enumerate(self.vetor):
            if v == elem:
                return i
        return -1

    def busca_por_index(self, index):
        if not (0 <= index < self.adicionados):
            raise ValueError("Posição inválida.")

        return self.vetor[index]

    def contem(self, elem):
        return self.busca(elem) > -1

    def ultimo_indice(self, elem):
        for i in range(self.adicionados - 1, -1, -1):
            if self.vetor[i] == elem:
                return i
        return -1

    def remove(self, elem=None, index=None):
        if index is not None:
            super().remove(index)
        elif elem is not None:
            index = self.busca(elem)
            if index != -1:
                super().remove(index)
            else:
                print("Elemento não encontrado.")
        else:
            raise ValueError("É necessário fornecer um elemento ou índice para remover.")

    def limpa(self):
        # Opção 1
        for i in range(self.adicionados):
            self.vetor[i] = None

        # Opção 2 (não utilizada)
        # self.vetor = [None] * len(self.vetor)

        self.adicionados = 0
