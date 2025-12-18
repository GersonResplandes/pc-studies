# Problema: O computador vai te dar um número inteiro N na primeira linha. Na segunda linha,
# ele vai te dar N números inteiros separados por espaço.
# Sua tarefa é imprimir a soma de todos esses números.

import sys

input = sys.stdin.readline
n = int(input())
y = list(map(int, input().split()))
if len(y) != n:
    print("Erro: número de elementos diferente do esperado.")
    sys.exit()
print(sum(y))
