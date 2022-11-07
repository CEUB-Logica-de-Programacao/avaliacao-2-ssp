# Os numerais romanos são representados por sete símbolos diferentes: I, V, X, L, C, D e M.
#
# | Símbolo | Valor |
# |---------|-------|
# | I       | 1     |
# | V       | 5     |
# | X       | 10    |
# | L       | 50    |
# | C       | 100   |
# | D       | 500   |
# | M       | 1000  |
#
# Por exemplo, 2 é escrito como II em algarismo romano, apenas dois juntos. 12 está escrito como XII,
# que é simplesmente X + II. O número 27 está escrito como XXVII, que é XX + V + II.
#
# Os numerais romanos são geralmente escritos da esquerda para a direita, do maior para a menor. Entretanto, o numeral
# para quatro não é IIII. Ao invés disso, o número quatro é escrito como IV. Porque o um está antes dos cinco,
# subtraindo-o, fazendo quatro. O mesmo princípio se aplica ao número nove, que é escrito como IX. Há seis casos em que a
# subtração é utilizada:
#
# * I pode ser colocado antes de V (5) e X (10) para fazer 4 e 9.
# * X pode ser colocado antes de L (50) e C (100) para fazer 40 e 90.
# * C pode ser colocado antes de D (500) e M (1000) para fazer 400 e 900.
#
# Dado um numeral romano, converta-o para um número inteiro.

def q4(numeral):
   def romanointeiro(self, s):
       val_rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
       val_int = 0
       for i in range(len(s)):
           if i > 0 and val_rom[s[i]] > val_rom[s[i - 1]]:
               val_int += val_rom[s[i]] - 2 * val_rom[s[i - 1]]
           else:
               val_int += val_rom[s[i]]
       return val_int
   A = input('digite o número romano: ')
   print(solução().romanointeiro(A))
        pass


if __name__ == '__main__':
    print(q4('MCMXCIV'))  # 1994
