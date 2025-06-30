'''
Esta será una calculadora, ademas de prácticas python otra vez
'''
def extraer_caracteres(a):
    caracteres = [x for x in a]
    espera = ''
    op = 0
    for relleno in caracteres:
        if relleno in '0123456789':
            espera += relleno
            caracteres.pop(0)
        else:
            break
    for cosa in caracteres:
        if cosa == '+':
            pass
        




print("Calculadora\n")
entrada = input(str('ingrese: '))
extraer_caracteres(entrada)
