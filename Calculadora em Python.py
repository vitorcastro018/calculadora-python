# Funções
def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def dividir(a, b):
    return a/b 
    
def multiplicar(a, b):
    return a*b

# Boas Vindas
print('''
    App desenvolvido por Vitor Castro

    Seja Bem vindo(a) a Calculadora,
    Nesse programa você poderá solucionar cálculos
    simples de matemática!

    ''')

# Programa
programa = True
while programa == True:


    operador = input('''
        
        Qual operação você deseja fazer?
        Responda somente com a letra:
        (a) Somar
        (b) Subtrair
        (c) Dividir
        (d) Multiplicar

    ''')
    # Validação da resposta
    while operador != 'a' and operador != 'b' and operador != 'c' and operador != "d":
        operador = input('''
            Por favor digite uma das opções acima!
        ''')
    # Chamada das Funções
    if operador == 'a':
        n1 = int(input('''
            Qual seu primeiro Número?
        '''))
        n2 = int(input('''
            Qual seu segundo Número?
        '''))
        
        resultado = int(somar(n1, n2))

        print(f'''
            O resultado de {n1} + {n2} = {resultado} 
        ''')
    elif operador == 'b':
        n1 = int(input('''
            Qual seu primeiro Número?
        '''))
        n2 = int(input('''
            Qual seu segundo Número?
        '''))
        
        resultado = subtrair(n1, n2)
        
        print(f'''
            O resultado de {n1} - {n2} = {resultado} 
        ''')


    elif operador == 'c':
        n1 = int(input('''
            Qual seu primeiro Número?
        '''))
        n2 = int(input('''
            Qual seu segundo Número?
        '''))

        resultado = dividir(n1, n2)

        print(f'''
            O resultado de {n1} / {n2} = {resultado} 
        ''')


    elif operador == 'd':
        n1 = int(input('''
            Qual seu primeiro Número?
        '''))
        n2 = int(input('''
            Qual seu segundo Número?
        '''))

        resultado = multiplicar(n1, n2)
        
        print(f'''
            O resultado de {n1} x {n2} = {resultado} 
        ''')


    # Final
    final = input('''

        Deseja Fazer outro Cálculo?
    (s) para sim
    (n) para não
    ''')
    programa = True if final == 's' else False

