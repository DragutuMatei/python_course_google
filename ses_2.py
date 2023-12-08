# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă
list2 = [7,2,9,4,9,34,68,5,3,6]

print(sorted(list2))

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
print(sorted(list2, reverse=True))

# afișarea numerelor cu indici pari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(list2[::2])

# afișarea numerelor cu indici impari din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)
print(list2[1::2])

# afișarea elementelor multipli ai lui 3
# I:
for nr in list2:
    if nr % 3 == 0:
        print(nr)
        
# II:
print([nr for nr in list2 if nr % 3 == 0])
    
    