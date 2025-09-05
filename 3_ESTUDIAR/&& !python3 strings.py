# Metodos de strings

# String de prueba llamado a
a = 'Nanche es un excelente acompañante en la vida'

# Imprimir el tamaño de la cadena
print(len(a))

# Convertir todo a mayusculas
print(a.upper())

# Convertir todo a minusculas
print(a.lower())

# Remplazar "excelente" por "perfecto" con .replace(palabra_vieja, palabra_nueva)
a = a.replace('excelente', 'perfecto')
print(a)

# Dividir una cadena de palabras con .split() dando un argumento para separar, en este caso un espacio ' '
# resulta en una lista de esas palabras
a = a.split(' ')
print(f'Tipo: {type(a)}\nLista: {a}')

# Une una lista de palabras poniendo un delimitador(que irá entre cada palabra), en este caso un '-'
# delimitador.join(palabras)
a_unido_guion = '-'.join(a)
print(a_unido_guion)
