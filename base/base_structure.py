class EstruturaEstatica:
    def __init__(self, capacidade):
        self.vetor = [None] * capacidade
        self.adicionados = 0

    def adiciona(self, elem, index=None):
        self._aumenta_capacidade()
        if index is None:
            self.vetor[self.adicionados] = elem
        else:
            if index < 0 or index > self.adicionados:
                raise ValueError("Posição inválida.")

            for i in range(self.adicionados, index, -1):
                self.vetor[i] = self.vetor[i - 1]

            self.vetor[index] = elem

        self.adicionados += 1

    def _aumenta_capacidade(self):
        current_size = len(self.vetor)
        if self.adicionados == current_size:
            bigger_vetor = [None] * (current_size * 2)

            for i, v in enumerate(self.vetor):
                bigger_vetor[i] = v
            self.vetor = bigger_vetor

    def remove(self, index):
        if not (0 <= index < self.adicionados):
            raise ValueError("Posição inválida.")

        for i in range(index, self.adicionados - 1):
            self.vetor[i] = self.vetor[i + 1]

        self.adicionados -= 1
        self.vetor[self.adicionados] = None  # Limpar a última posição

    def is_vazia(self):
        return self.adicionados == 0

    def __len__(self):
        return self.adicionados

    def __str__(self):
        s = "["
        for _, v in enumerate(self.vetor):
            if v is None:
                continue
            s += str(v) + ", "

        if self.adicionados > 0:
            s = s[:-2]  # Remover a última vírgula e espaço

        s += "]"
        return s
