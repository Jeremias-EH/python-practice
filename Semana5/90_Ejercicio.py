"""
Comprobare si una palabra es palindromo usando lambda
"""

palindromo = lambda palabra: palabra == palabra[::-1]

print(palindromo('rama'))
print(palindromo('radar'))