'''
Conjuntos: coleccion de elementos desordenados y que no permiten duplicados, es como un conjunto matematico.
Las operaciones de pertenencia son mas rapidas que las listas
'''
def conjuntos():
    c1 = [1, 2, 3, 4, 5, 1, 3, 4]
    print(f'Lista con duplicados: {c1}')
    c1 = set(c1)
    print(f'Eliminar duplicados: {c1}')

    c2 = {1, 6, 3}
    c3 = {1, 5, 2, 6, 3, 7}
    print(f'c2: {c2}\nc3: {c3}')
    union = c2 | c3
    interseccion = c2 & c3
    print(f'union: {union}\nintersección: {interseccion}')


'''
Diccionarios: coleccion de pares clave valor, cada clave debe ser unica y sirve para acceder a el valor asociado
'''
def diccionarios():
    contactos = {
        'abril' : '1234567890',
        'julio' : '0987654321',
        'march' : '1324354657',
        'josue' : '0897867564'
    }
    print(f'Diccionario contactos: {contactos}')
    print(f'Acceder al número de abril: {contactos['abril']}\nAgregar el número de ambar: 2435465768')
    contactos['ambar'] = '2435465768'
    print(f'Diccionario actualizado: {contactos}\nActualizar el numero de julio por: 7564534231')
    contactos['julio'] = '7564534231'
    print(f'Diccionario actualizado: {contactos}\nEliminar el contacto de march')
    del contactos['march']
    print(f'Diccionario actualizado: {contactos}')
    
    print('Todos los contactos')
    for nombre, numero in contactos.items():
        print(f'\nNombre: {nombre};Número: {numero}')
    

diccionarios()
