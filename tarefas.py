#Variaveis
num_a = 5
num_b = 6

#Funcao para somar dois numeros

def somar_numeros(numA, numB):
    soma = numA + numB
    return soma

resultado_da_soma = somar_numeros(num_a,num_b)

#Funcao para multiplicar dois numeros

def multiplicar_numeros(numA, numB):
    multiplica = numA * numB
    return multiplica

resultado_da_multiplicacao = multiplicar_numeros(num_a, num_b)

#Funcao para imprimir o resultado das funções de soma e multiplicação

def exibir_resultados(resultado):
    print(resultado)

exibir_resultados(f'soma: {num_a} + {num_b} = {resultado_da_soma}')
exibir_resultados(f'multiplicao: {num_a} x {num_b} = {resultado_da_multiplicacao}')