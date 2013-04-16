# coding: utf-8

# tworzymy pięć teczek dla pięciu osób
# każda osoba opisana jest za pomocą takich atrybutów:
#   0 --> imię
#   1 --> nazwisko
#   2 --> wiek
#   3 --> lista imion dzieci
#   4 --> zawód
osoba1 = ['Jan'      , 'Kowalski'  , 23, ['Jasio']                         , 'Programista']
osoba2 = ['Anna'     , 'Nowak'     , 50, ['Kasia', 'Wiola']                , 'Programistka']
osoba3 = ['Stanisław', 'Wiśniewski', 54, []                                , 'Malarz']
osoba4 = ['Wioletta' , 'Hałas'     , 63, ['Zbigniew']                      , 'Wiolonczelistka']
osoba5 = ['Frania'   , 'Guzik'     , 28, ['Jagna', 'Magda', "Dorota"]      , 'Architektka']

# zbieramy wszystkie te osoby w jedną listę ziomów
ziomy = [ osoba1, osoba2, osoba3, osoba4, osoba5 ]

# przyjrzyjmy się każdemu ziomów
for ziomek in ziomy:
    # wyjmujemy sobie listę dzieci danego ziomka
    dzieci = ziomek[3]

    # jeśli dzieci więcej niż jedno, wypisz wszystkie ich imiona
    if len(dzieci) > 1:
        print "Niezły urodzaj: " + ", ".join(dzieci)
    # w przeciwnym razie, jeśli (elif) ma jedno dziecko, wypisz jego imię
    elif len(ziomek[3]) is 1:
        print "O masz dziecko: " + dzieci[0]
    # jeśli w ogóle nie ma dzieci, to powiedz, jak ma na nazwisko
    else:
        print "Kto nie ma dzieci? " + ziomek[1]

# odstęp wielokreskowy
print '_' * 50

# przygotowujemy sobie puste kubełki, żeby pogrupować naszych ziomków
urodzaj = []
dwoje   = []
jedno   = []
zero    = []

# i znów przyjrzymy się im ziomek po ziomku
for ziomek in ziomy:
    # liczba dzieci
    dzieci = len(ziomek[3])
    # wiek ziomka
    wiek   = ziomek[2]

    # jeśli ma więcej niż dwójkę dzieli LUB ma poniżej 30 lat
    if dzieci > 2 or wiek < 30:
        # dodaj go do kubełka "urodzaj"
        urodzaj.append(ziomek)
    # w przeciwnym wypadku, jeśli (elif) ma dokładnie dwójkę dzieci
    elif dzieci is 2:
        # dodaj go do kubełka "dwoje"
        dwoje.append(ziomek)        
    # w przeciwnym wypadku, jeśli (elif) ma dokładnie jedno dziecko
    elif dzieci is 1:
        # dodaj go do kubełka "dwoje"
        jedno.append(ziomek)
    # jeśli to żaden z powyższych przypadków (czyli w ogóle nie ma dzieci)
    else:
        # dodaj go do kubełka "zero"
        zero.append(ziomek)

# ukladamy sobie kubełki w kolejności malejącej
posortowane = [ urodzaj, dwoje, jedno, zero ]

# dla każdego kubełka na tej liście
for kubelek in posortowane:
    # najpierw narysujemy odkresownik
    print "|" * 50

    # a później wypiszemy imię każdego ziomka w tym kubełku
    for ziomek in kubelek:
        print ziomek


# odstęp wielokreskowy
print '_' * 50

# sprawdzamy każdego ziomka na naszej liście ziomów
for ziomek in ziomy:
    # pytamy go o imiona dzieci
    dzieci = ziomek[3]

    # bierzemy imię każdego z jego dzieci
    for dziecko in dzieci:
        # sprawdzamy czy jego/jej imię zawiera (in) literę 'g'
        if 'g' in dziecko:
            # jeśli tak, to wypisujemy nazwisko zioma i imię dziecka
            print ziomek[1] + ": " + dziecko

