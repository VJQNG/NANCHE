# Metodos de strings

# String de prueba llamado a
a = 'Nanche es un excelente acompañante en la vida'

# Imprimir el tamaño de la cadena
print(f'Tamaño de la cadena: {len(a)}')

# Convertir solo el primer caracter en mayuscula y el resto en minuscula
print(f'Convertir el primer caracter en mayuscula de "nanche es precioso": {'nanche es precioso'.capitalize()}')

# Convertir todo a mayusculas
print(f'Convertir todo a mayusculas: {a.upper()}')

# Convertir todo a minusculas
print(f'Convertir todo a minusculas: {a.lower()}')

# Remplazar "excelente" por "perfecto" con CADENA.replace(PALABRA_VIEJA, PALABRA_NUEVA)
a = a.replace('excelente', 'perfecto')
print(f'Remplazar "Excelente" por "Perfecto": {a}')

# Dividir una cadena de palabras con .split() dando un argumento para separar, en este caso un espacio ' '
# resulta en una lista de esas palabras
# CADENA.split(SEPARADOR)
a = a.split(' ')
print(f'Tipo: {type(a)} Lista: {a}')

# Une una lista de palabras poniendo un delimitador(que irá entre cada palabra), en este caso un '-'
# DELIMITADOR.join(PALABRAS)
a_unido_guion = '-'.join(a)
print(f'Unir la lista anterior de palabras separados por un "-": {a_unido_guion}')

# Estos devuelven True o False
# Verificar si una cadena comienza o termina con una subcadena especifica; CADENA.startswith(SUBCADENA); CADENA.endswith(SUBCADENA)
a = 'Nanche es un excelente acompañante en la vida'
print(f'Verificar que la cadena empiece con "Nanche": {a.startswith('Nanche')}')
print(f'Verificar que la cadena termine con "vida": {a.endswith('vida')}')

# Verificar si todos los elementos de una cadena con mayusculas o minusculas
# CADENA.isupper(); CADENA.islower()
b = 'NANCHE'
c = 'nanche'
print(f'Verificar que todos los elementos de "NANCHE" son mayusculas: {'NANCHE'.isupper()}')
print(f'Verificar que todos los elementos de "nanche" son minusculas: {'nanche'.islower()}')

# Verificar si la cadena contiene solo caracteres alfabeticos y no esta vacia
# CADENA.isalpha()
print(f'Verificar si la cadena "nanche16" contiene solo caracteres alfabeticos y no esta vacia: {'nanche16'.isalpha()}')

# Verificar si la cadena contiene solo digitos numericos y no esta vacia
# CADENA.isdigit()
print(f'Verificar si la cadena "1234" contiene solo digitos numericos y no esta vacia: {'1234'.isdigit()}')

# Eliminar caracteres de los extremos de la cadena; por defecto elimina espacios o se puede dar una subcadena para eliminar
# CADENA.strip() o CADENA.strip(SUBCADENA)
print(f'Eliminar los espacios de los extremos "  nanche  ": {'  nanche  '.strip()}')
print(f'Eliminar "---" de "---nanche---": {'---nanche---'.strip('-')}')
# Misma idea por defecto o con SUBCADENA solo que por la izquierda o derecha: CADENA.lstrip() o CADENA.strip()

# Buscar una subcadena dentro de una cadena y devuelve el indice de su primera aparicion o -1 si no se encuentra
# o decirle desde que indice comience a buscar, START Y STOP son opcionales
# CADENA.find(SUBCADENA, START, STOP)
a = 'Nanche es un excelente acompañante en la vida'
print(a)
print(f'Buscar "un" en la cadena anterior: {a.find('un')}')
print(f'Buscar "un" desde la posicion 11: {a.find('un', 11)}')
# faltan más...
