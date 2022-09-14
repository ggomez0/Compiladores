#Importar librerias
import sys
import ply.lex as lex


#Tokens
tokens = ["palabra", "tagstart","tagend"]


t_palabra = r'([a-z|A-Z|0-9|_|.|,|¡|!|¿|?|"|\'|(|)|{|}|[|\]|\s])+'
t_tagstart = r'[<][([a-z|A-Z|0-9)]*[>]'
t_tagend = r'[<][/][([a-z|A-Z|0-9)]*[>]'



# Definir la función t_error para el tratamiento de errores.
def t_error(t):
    print(f"ERROR: la cadena {t.value} no es aceptada")
    t.lexer.skip(len(t.value))


# Definir la función t_newline para el contador de linea   
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


#Definir la funcion para leer el .txt
def leerTxt():
    try:
        filename = open('C:/Users/gaspa/Desktop/ejercicio5.txt', 'r')
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
    print('-------------------------------------------')
    tok = lexer.token()
    if not tok:
        break
    print('(', tok.type, ',', tok.value, ',', tok.lineno, ')')
