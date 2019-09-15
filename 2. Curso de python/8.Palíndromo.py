# -*- coding: utf-8 -*-

def palindrome2(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    return False

def palindrome(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0,letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    else:
        return False

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))
    result = palindrome2(word)
    if result == True:
        print('La palabra {} es un palpíndromo'.format(word))
    else:
        print('La palabra {} NO es un palíndromo'.format(word))
