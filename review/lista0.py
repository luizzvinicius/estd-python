# Armazena uma lista todos os múltiplos de 3,entre 1 e 100. Imprima cada elemento da lista, um por linha.
multiple3 = [i for i in range(0, 100, 3)]
print(multiple3)

for i in range(1, 6):
    for j in range(i):
        print((j + 1) * i, end=" ")
    print()


dia_semana = 7
match dia_semana:
    case 0:
        print("segunda")
    case _:
        print("indefinido")