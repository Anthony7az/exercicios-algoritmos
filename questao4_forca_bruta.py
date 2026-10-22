
def busca_forca_bruta(dna, procurada):
    n = len(dna)
    m = len(procurada)

    for i in range(n - m + 1):
        j = 0

        while j < m and dna[i + j] == procurada[j]:
            j += 1

        if j == m:
            return i + 1

    return -1


dna = input().strip().upper()
procurada = input().strip().upper()

posicao = busca_forca_bruta(dna, procurada)

if posicao != -1:
    print(f"Sequência encontrada na posição {posicao}.")
else:
    print("Sequência não encontrada.")
