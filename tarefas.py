#Funcao para somar dois numeros

def somar_numeros(numA, numB):
    soma = numA + numB
    return soma

resultado_da_soma = somar_numeros(5,15)

#Funcao para multiplicar dois numeros

def multiplicar_numeros(numA, numB):
    multiplica = numA * numB
    return multiplica

resultado_da_multiplicacao = multiplicar_numeros(5, 5)

#Funcao para imprimir o resultado das funções de soma e multiplicação

def exibir_resultados(resultado):
    print(f' {resultado}')

exibir_resultados(f'soma {resultado_da_soma}')
exibir_resultados(f'multiplicao {resultado_da_multiplicacao}')