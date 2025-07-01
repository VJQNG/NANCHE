'''
Esta será una calculadora, ademas de practicar python otra vez.
'''
def extraer_caracteres(a):
    c = [x for x in a]
    espera = ''
    op = 0
    print(c)
    for relleno in c:
        if relleno in '+-*/':
            print(f'caracteres: {c}, espera: {espera}')
            break
        else:
            print(f'caracteres: {c}, espera: {espera}')
            espera += relleno
            c.pop(0)
            print(f'caracteres: {c}, espera: {espera}')






print("Calculadora\n")
entrada = input(str('ingrese: '))
extraer_caracteres(entrada)
