# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# Código:

# def pertence_fibonacci(numero):
    
#     a, b = 0, 1
#     while b <= numero:
#         if b == numero:
#             return True
#         a, b = b, a + b
#     return False

# num = int(input("Digite um número: "))

# # Chama a função e imprime o resultado
# if pertence_fibonacci(num):
#     print(f"O número {num} pertence à sequência de Fibonacci.")
# else:
#     print(f"O número {num} não pertence à sequência de Fibonacci.")

###################################################################################

# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# Código:

# def contar_as(texto):
#     """Conta a quantidade de vezes que a letra 'a' aparece em um texto, 
#     ignorando maiúsculas e minúsculas. """

#     # Converter todo o texto para minúsculas para facilitar a contagem
#     texto_minusculo = texto.lower()
#     # Contar a ocorrência da letra 'a'
#     contagem = texto_minusculo.count('a')
#     return contagem

# texto = input("Digite um texto: ")
# quantidade_as = contar_as(texto)

# if quantidade_as > 0:
#     print(f"A letra 'a' aparece {quantidade_as} vezes no texto.")
# else:
#     print("A letra 'a' não foi encontrada no texto.")

###################################################################################

# 3) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

# Código:

# INDICE = 12
# SOMA = 0
# K = 0

# while K < INDICE:
#     K = K + 1
#     SOMA = K + SOMA
    
# print(SOMA)

# SOMA irá imprimir 78

###############################################################################

# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

# Resposta:

# a) 1, 3, 5, 7 = 9
# b) 2, 4, 8, 16, 32, 64 = 128
# c) 0, 1, 4, 9, 16, 25, 36 = 49
# d) 4, 16, 36, 64 = 100
# e) 1, 1, 2, 3, 5, 8 = 13
# f) 2, 10, 12, 16, 17, 18, 19 = 23

###############################################################################

# 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 

# Resposta:

# Primeiro ligar um interruptor e esperar uns minutos até que a lâmpada esquente, depois desligar e ligar outro interruptor.
# Na segunda visita verificar qual a lâmpada quente, qual a lâmpada acessa e qual a lâmpada fria que você descobrirá quais os interruptores para suas respectivas lâmpadas.