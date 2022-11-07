# Você recebe uma lista de nomes, e uma lista de alturas que consiste de números inteiros positivos distintos.
# Ambas as listas são de comprimento `n`.
#
# Para cada índice `i`, `nomes[i]` e `alturas[i]` denotam o nome e a altura da i-ésima pessoa.
#
# Retorne os nomes ordenados em ordem decrescente pelas alturas das pessoas.
#
# ### Exemplo 1
#
# ```
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# ```
#
# ### Exemplo 2
#
# ```
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# ```

lis_nome=[]
lis_altura=[]
while True:
    print("adicionar pesso--1")
    print('finalisar ---2')
    x=int(input('resposta'))
    if x==2:
        break
    nome=str(input('nome: '))
    altura=float(input('altura: '))
    lis_nome.append(nome)
    lis_altura.append(altura)
    
for j in range(len(lis_altura)):
    for i in range(j+1,len(lis_altura)):
        if lis_altura[j]<lis_altura[i]:
            lis_nome[i],lis_nome[j]=lis_nome[j],lis_nome[i]
print(lis_nome)
    pass

if __name__ == '__main__':
    print(q1(["Mary", "John", "Emma"], [180, 165, 170]))
