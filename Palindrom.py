# Zadanie palindrom

def czy_palindrom(word):
    if word.lower() == word[::-1].lower():
       print(f"Słowo: {word} to palindrom!")
    else:
       print(f"Słowo: {word} nie jest palindromem.")

czy_palindrom('Ania') # Tu wpisz słowo, aby sprawdzić czy to palindrom.