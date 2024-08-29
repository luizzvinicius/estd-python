# Crie suas próprias funções, não utilize funções preexistentes da linguagem


def palindroma(word: str):
    return word == word[::-1]


def last_string(frase: str):
    size = len(frase) - 1
    last_word_size = 0

    for letter in frase[::-1]:
        if letter == " ":
            break
        last_word_size += 1

    return frase[size - last_word_size + 1 : :]


# As normas para a exibição da bibliografia de um artigo científico exigem que o
# nome do autor seja escrito no formato último sobrenome, sequência das primeiras letras do nome e dos demais
# sobrenomes, seguidas de ponto final. Por exemplo, Antônio Carlos Jobim seria referido por Jobim, A. C..
# Escreva um programa que receba um nome e o escreva no formato de bibliografia.


def cientific_name(name: str):
    resto = ""
    last_blank_space = 0

    for i, letter in enumerate(name.strip()):
        if letter == " ":
            last_blank_space = i
            resto += f"{name[i + 1]}."

    return f"{name[last_blank_space + 1 : :]}, {name[0]}. {resto[0 : len(resto) - 2]}"
