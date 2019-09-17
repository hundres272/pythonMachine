"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char (char_sequence):
    for i in char_sequence:
        cont = 0
        for j in char_sequence:
            if i == j:
                cont += 1
        if cont == 1:
            return i
    return '_'


if __name__ == '__main__':
    char_sequence = str(input ('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char (char_sequence)

    if result == '_':
        print ('Todos los caracteres se repiten.')
    else:
        print ('El primer caracter no repetido es: {}'. format(result))
