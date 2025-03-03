# Zadanie palindrom

def czy_palindrom(word):
    inverted = word[::-1]
    palidrom = word.lower() == inverted.lower()

    if palidrom:
        print(f"Słowo: {word} to palindrom!")
    else:
        print(f"Słowo: {word} nie jest palindromem.")

czy_palindrom('Anna') # Tu wpisz słowo, aby sprawdzić czy to palindrom.