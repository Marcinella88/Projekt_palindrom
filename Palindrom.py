# Zadanie palindrom

def czy_palindrom(word): 
    return word.lower() == word[::-1].lower()

if czy_palindrom('Anna'):                        # Tu wpisz słowo, aby sprawdzić czy to palindrom. 
    print(f"Słowo to palindrom!")       
else:
    print(f"Słowo to nie palindrom!")