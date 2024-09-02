def reverse_word(word: str):
    if len(word) == 0:
        return word

    return word[len(word) - 1] + reverse_word(word[0 : len(word) - 1])


count = 0


def count_letter(word: str, letter: str):
    global count
    if len(word) == 0:
        return 0

    if word[0] == letter:
        count += 1

    count_letter(word[1:], letter)
    return count


# Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente.
count_crescente = 0


def crescente_numbers(num: int, i: int):
    print(i)
    if i == num:
        return
    return crescente_numbers(num, i + 1)


# Escreva uma função recursiva que informa se uma String é palíndroma ou não.


def palindromo(word: str):
    if len(word) == 0:
        return
    if word[0] != word[-1]:
        return False

    palindromo(word[1 : len(word) - 1])
    return True


# fibonacci recursivo


def fib(n: int, a: int = 0, b: int = 1, s: int = 0, cont: int = 0):
    if cont == n:
        return a
    s = a + b
    a = b
    b = s
    cont += 1
    return fib(n, a, b, s, cont)


print(fib(8))
