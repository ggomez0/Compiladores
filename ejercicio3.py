#Alumno:Gaspar Gomez

# Importar librerias
import sys
import ply.lex as lex

#tokens
tokens = ["empiezauno","empiezacero"]

#empieza con 1 cualquier numero entremedio y termina con doble cero
t_empiezauno = r'([1][0|1|2|3|4|5|6|7|8|9]*[0][0])'

#empieza con 0 cualquier numero entremedio y termina con doble uno
t_empiezacero = r'([0][0|1|2|3|4|5|6|7|8|9]*[1][1])'

#ignora espacios vacios
t_ignore = r'[ ]+'

# Definir la función t_error para el tratamiento de errores.
def t_error(t):
    print(f"ERROR: la cadena {t.value} no es aceptada")
    t.lexer.skip(len(t.value))

# Definir la función t_newline para el contador de linea   
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

#leer el txt
def leerTxt():
    try:
        filename = open('C:/Users/gaspa/Desktop/ejercicio3.txt', 'r')
        data = filename.read()
        filename.close()
        return data
    except:
        sys.stdout.write('Error al leer el archivo \n')
        data = sys.stdin.read()
        return data

# Construcción del analizador léxico

lexer = lex.lex()
lexer.input(leerTxt())

# Identifica tokens
print('Token - Lexema - Linea')
while True:
    print ('------------------------------------------')
    tok = lexer.token()
    if not tok: break
    print('(', tok.type, ',', tok.value, ',', tok.lineno, ')')
