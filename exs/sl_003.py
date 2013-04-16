zabawki = ['kaczka', 'kochajek', 'zółto-czerwona krowa', 'sowa', 'krokodyl']

# dorzucamy na koniec pieska
zabawki.append('piesek')

# wyciągamy z tej listy krowę
krowa = zabawki[2]
print krowa

# zamieniamy krowę na kochajka!
zabawki_bez_krowy = zabawki[:2] + ['kochajek'] + zabawki[3:]
print zabawki_bez_krowy

# wydobywamy kolor krowy
rozbita_krowa = krowa.split()
kolor_krowy   = rozbita_krowa[0]
print kolor_krowy
