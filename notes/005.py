# zajrzyjmy do wielkiego pudła z zabawkami
pudlo = ["czerwony kotek", "niebieski samochodzik", "niebieski balonik",
         "drewniany, zielony kwiatek", "lalka w czerwonym kubraczku"]

# weźmy też trzy mniejsze pudełka, do których "posprzątamy" zabawki
niebieskie = []
czerwone   = []
zielone    = []

print "- Marysiu, przynieś mi zabawki z tego pudła."
print "  Tylko przynieś po jednym, żebyś się nie przewróciła!"
print ""

# Marysia idzie po zabawki
for zabawka in pudlo:
    print "Marysia, tupi tupi, idzie do pudła."
    print "- O, " + zabawka + ". Malysia niesie tatusiowi!"

    # jeśli nazwa zabawki zaczyna się od 'niebieski'    
    if zabawka.startswith('niebieski'):
        print "- Świetnie, wrzucimy to do niebieskiego pudła."
        # dołóż ją do pudła niebieskiego (dodaj na koniec listy)
        niebieskie.append(zabawka)

    # w przeciwnym razie, jeśli (elif)
    # w jej nazwie występuje słowo 'czerwony'
    elif 'czerwony' in zabawka:
        print "- Ta zabawka trafi do czerwonego pudełka."
        # dołóż ją do pudła czerwonego (dodaj na koniec listy)
        czerwone.append(zabawka)

    # w przeciwnym razie (else) nie ma znaczenia jaki ma kolor
    # my wiemy, że to musi być 'zielony'
    else:
        print "- Lubisz zielony, prawda? Jak las!"
        # dołóż ją do pudła zielonego (dodaj na koniec listy)
        zielone.append(zabawka)

    # odstęp dla łatwiejszego czytania wyników
    print ""

# kreską oddzielimy sprzątanie zabawek od oglądania zabawek
print "- " * 10
print ""

print '- Chodź Marysiu, pobawimy się czerwonymi zabawkami'
print '- Malysia zagląda. O, ' + ', '.join(czerwone)

print ''
print '- No to teraz zajrzyjmy do zielonych'
print '- Malysia widzi ' + zielone[0]

print ''
print '- A tutaj w niebieskich ile jest zabawek'
print '- Tsy!'
print '- Nie, nie Marysiu, ' + str(len(niebieskie)) + '!'


    

