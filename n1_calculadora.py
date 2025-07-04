'''
Esta será una calculadora, ademas de practicar python otra vez.
'''
def extraer_caracteres(a):
    c = [x for x in a] # lista de valores ingresados por el usuario.
    espera = '' # primer operando para hacer el siguiente.
    op = 0 # guarda la operacion
    for pos in c:
        if(pos in '+-*/'):
            print(f'caracteres break: {c}, espera: {espera}') 
            del c[0:len(espera)+1]
            print(c)
            for hacer in range(len(c)):
                match hacer:
                    case '+':
                        pass
            break
        else:
            espera += pos

print("Calculadora\n")
entrada = input(str('ingrese: '))
extraer_caracteres(entrada)
