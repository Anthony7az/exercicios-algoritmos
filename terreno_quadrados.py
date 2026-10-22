def calcular_mdc(L, A):
    if A == 0:
        return L

    return calcular_mdc(A, L % A)


L = int(input("Digite a largura do terreno: "))
A = int(input("Digite a altura do terreno: "))

lado = calcular_mdc(L, A)

print("Tamanho do lado dos quadrados:", lado)
