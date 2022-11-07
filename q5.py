# Você recebe uma lista de caminhos, onde `caminhos[i] = [cidadeAi, cidadeBi]` significa que existe um caminho direto que
# vai de `cidadeAi` para `cidadeBi`. Retorne a cidade de destino, ou seja, a cidade sem nenhum caminho que saia dela.
#
# ### Exemplo 1
#
# ```
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo"
# Explicação: Através de "London" -> "New York" -> "Lima" -> "Sao Paulo", você chega ao destino.
# ```
#
# ### Exemplo 2
#
# ```
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explicação: Todos os caminhos possíveis são:
# "D" -> "B" -> "C" -> "A".
# "B" -> "C" -> "A".
# "C" -> "A".
# "A".
# Portanto, "A" é a cidade de destino.
# ```

def q5(paths):
    ComS = []
    SemS = []
    for i, x in enumerate(paths):
        ComS.append(paths[i][0])
        for i, x in enumerate(paths):
            if paths[i][1] not in ComS:
                SemS.append(paths[i][1])
        return SemS[0]


if __name__ == '__main__':
    print(q5([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
