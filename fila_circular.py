class FilaCircular:
    def __init__(self, tamanho):
        self.primeiro = 0
        self.ultimo = 0
        self.lista = [None] * (tamanho + 1)

    def enfileira(self, elem):
        if (self.ultimo + 1) % len(self.lista) == self.primeiro:
            raise Exception("Fila cheia")

        self.lista[self.ultimo] = elem
        self.ultimo = (self.ultimo + 1) % len(self.lista)

    def desenfileira(self):
        if len(self.lista) == 0:
            raise Exception("Fila vazia")

        self.primeiro = (self.primeiro + 1) % len(self.lista)

    def __str__(self) -> str:
        string = "["
        i = self.primeiro
        while i != self.ultimo:
            string += str(self.lista[i]) + ", "
            i = (i + 1) % len(self.lista)

        return f"{string[:-2]}]"


fila = FilaCircular(5)

fila.enfileira(1)
fila.enfileira(2)
fila.desenfileira()

print(fila)
