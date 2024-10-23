class No:
    def __init__(self, elem, proximo=None):
        self.elem = elem
        self.proximo = proximo

    def get_elem(self):
        return self.elem

    def set_elem(self, elem):
        self.elem = elem

    def get_proximo(self):
        return self.proximo

    def set_proximo(self, proximo):
        self.proximo = proximo

    def __str__(self):
        return f"No [elem={self.elem}, proximo={self.proximo}]"


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.ultimo = None
        self.tamanho = 0

    def adiciona(self, elem):
        no = No(elem)
        if self.tamanho == 0:
            self.inicio = no
        else:
            self.ultimo.set_proximo(no)
        self.ultimo = no
        self.tamanho += 1

    def adiciona_inicio(self, elem):
        if self.tamanho == 0:
            self.adiciona(elem)
        else:
            novo_elem = No(elem, self.inicio)
            self.inicio = novo_elem
            self.tamanho += 1

    def adiciona_index(self, elem, index):
        if index < 0 or index > self.tamanho:
            raise ValueError("Índice inválido")

        if index == 0:
            self.adiciona_inicio(elem)
        elif index == self.tamanho:
            self.adiciona(elem)
        else:
            novo_no = No(elem)
            inicial = self.inicio
            for i in range(index):
                if i + 1 == index:
                    novo_no.set_proximo(inicial.get_proximo())
                    inicial.set_proximo(novo_no)
                inicial = inicial.get_proximo()
            self.tamanho += 1

    def index(self, elem):
        inicial = self.inicio
        for i in range(self.tamanho):
            if inicial.get_elem() == elem:
                return i
            inicial = inicial.get_proximo()
        return -1

    def _busca_no(self, index):
        self.valida_index(index)

        start = self.inicio
        for _ in range(index):
            start = start.get_proximo()
        return start

    def busca(self, index):
        return self._busca_no(index).get_elem()

    def remove_index(self, index):
        self.valida_index(index)

        if index == 0:
            self.remove_first()
        elif index == self.tamanho - 1:
            self.remove_last()
        else:
            anterior_ao_removido = self._busca_no(index - 1)
            ser_removido = anterior_ao_removido.get_proximo()
            retorno = ser_removido.get_elem()
            anterior_ao_removido.set_proximo(ser_removido.get_proximo())
            ser_removido.set_proximo(None)
            ser_removido.set_elem(None)
            self.tamanho -= 1
            return retorno

    def remove_first(self):
        if self.tamanho == 0:
            raise RuntimeError("Lista está vazia")

        inicial = self.inicio
        removido = self.inicio.get_elem()
        self.inicio = self.inicio.get_proximo()
        inicial.set_elem(None)
        inicial.set_proximo(None)
        self.tamanho -= 1
        return removido

    def remove_last(self):
        if self.tamanho == 0:
            raise RuntimeError("Lista está vazia")
        if self.tamanho == 1:
            return self.remove_first()

        penultimo_no = self._busca_no(self.tamanho - 2)
        removido = self.ultimo.get_elem()
        self.ultimo.set_elem(None)
        self.ultimo = penultimo_no
        penultimo_no.set_proximo(None)
        self.tamanho -= 1
        return removido

    def remove(self, elem):
        index = self.index(elem)
        if index == -1:
            return
        self.remove_index(index)

    def inverte_lista(self):
        anterior = None
        proximo = None

        atual = self.inicio
        while atual is not None:
            proximo = atual.get_proximo()
            atual.set_proximo(anterior)
            anterior = atual
            atual = proximo

        self.inicio = anterior

    def to_vector(self):
        if self.tamanho == 0:
            return []

        vetor = [None] * self.tamanho

        atual = self.inicio
        for i in range(self.tamanho):
            vetor[i] = atual.get_elem()
            atual = atual.get_proximo()
        return vetor

    def adiciona_ordenado(self, elem):
        inicial = self.inicio
        i = 0
        while i < self.tamanho:
            if elem < inicial.get_elem():
                break
            inicial = inicial.get_proximo()
            i += 1

        self.adiciona_index(i, elem)

    def get_first(self):
        if self.inicio is None:
            raise ValueError("Elemento é null")
        return self.inicio

    def get_last(self):
        if self.ultimo is None:
            raise ValueError("Elemento é null")
        return self.ultimo

    def limpa(self):
        atual = self.inicio
        while atual is not None:
            proximo = atual.get_proximo()
            atual.set_elem(None)
            atual.set_proximo(None)
            atual = proximo
        self.tamanho = 0

    def ordena(self): # bubble
        inicial = self.inicio
        proximo = None
        for _ in range(self.tamanho - 1):
            for _ in range(self.tamanho - 1):
                proximo = inicial.get_proximo()
                if inicial.get_elem() > proximo.get_elem():
                    elem_inicial = inicial.get_elem()
                    inicial.set_elem(proximo.get_elem())
                    proximo.set_elem(elem_inicial)
                inicial = proximo
            inicial = self.inicio

    def valida_index(self, index):
        if not 0 <= index < self.tamanho:
            raise ValueError("Índice inválido")

    def __len__(self):
        return self.tamanho

    def __str__(self):
        if self.tamanho == 0:
            return "[]"

        s = "["
        atual = self.inicio
        for _ in range(self.tamanho - 1):
            s += f"{atual.get_elem()}, "
            atual = atual.get_proximo()

        s += f"{atual.get_elem()}]"
        return s
