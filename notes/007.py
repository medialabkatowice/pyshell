# coding: utf-8
# nasze dane to średnie wilgotności i temperatury w Dąbrowie 
# Górniczej w kolejnych miesiącach lat 2009-2011. 
# Tabela posiada następujące kolumny:
#   - nazwa miejscowości
#   - rok
#   - miesiac
#   - wilgotność (%)
#   - temperatura
# Dane pochodzą ze strony: http://stacje.katowice.pios.gov.pl/monitoring/
dane = [
    ["Dąbrowa Górnicza", 2009,  1, 92, -5.6],
    ["Dąbrowa Górnicza", 2009,  2, 94, -3.7],
    ["Dąbrowa Górnicza", 2009,  3, 88, -0.1],
    ["Dąbrowa Górnicza", 2009,  4, 55, 10.3],
    ["Dąbrowa Górnicza", 2009,  5, 68, 11.9],
    ["Dąbrowa Górnicza", 2009,  6, 82, 13.1],
    ["Dąbrowa Górnicza", 2009,  7, 73, 17.4],
    ["Dąbrowa Górnicza", 2009,  8, 77, 16.6],
    ["Dąbrowa Górnicza", 2009,  9, 84, 13.1],
    ["Dąbrowa Górnicza", 2009, 10, 93, 5.0],
    ["Dąbrowa Górnicza", 2009, 11, 92, 3.4],
    ["Dąbrowa Górnicza", 2009, 12, 94, -2.7],
    ["Dąbrowa Górnicza", 2010,  1, 95, -8.1],
    ["Dąbrowa Górnicza", 2010,  2, 91, -3.5],
    ["Dąbrowa Górnicza", 2010,  3, 77, 1.3],
    ["Dąbrowa Górnicza", 2010,  4, 75, 6.6],
    ["Dąbrowa Górnicza", 2010,  5, 92, 9.9],
    ["Dąbrowa Górnicza", 2010,  6, 77, 15.1],
    ["Dąbrowa Górnicza", 2010,  7, 79, 18.4],
    ["Dąbrowa Górnicza", 2010,  8, 87, 15.9],
    ["Dąbrowa Górnicza", 2010,  9, 91, 9.4],
    ["Dąbrowa Górnicza", 2010, 10, 89, 3.4],
    ["Dąbrowa Górnicza", 2010, 11, 94, 4.3],
    ["Dąbrowa Górnicza", 2010, 12, 98, -6.6],
    ["Dąbrowa Górnicza", 2011,  1, 97, -2.7],
    ["Dąbrowa Górnicza", 2011,  2, 89, -4.4],
    ["Dąbrowa Górnicza", 2011,  3, 77, 1.9],
    ["Dąbrowa Górnicza", 2011,  4, 72, 9.0],
    ["Dąbrowa Górnicza", 2011,  5, 74, 12.0],
    ["Dąbrowa Górnicza", 2011,  6, 81, 16.4],
    ["Dąbrowa Górnicza", 2011,  7, 89, 15.3],
    ["Dąbrowa Górnicza", 2011,  8, 84, 17.3],
    ["Dąbrowa Górnicza", 2011,  9, 85, 13.4],
    ["Dąbrowa Górnicza", 2011, 10, 92, 6.7],
    ["Dąbrowa Górnicza", 2011, 11, 93, 0.9],
    ["Dąbrowa Górnicza", 2011, 12, 97, -0.1],
]

# chcielibyśmy zebrać w jednym miejscu średnie temperatury dla każdego roku
# w tym celu zbierzemy temperatury każdego roku w osobną listę:
#
#   srednie = [
#       [ -5.6, -3.7, -0.1, ... -2.7 ],
#       [ -8.1, -3.5, 1.3 ... -6.6 ],
#       [ -2.7, -4.4, 1.9 ... -0.1 ]
#   ]
#
# Dzięki temu będziemy mogli łatwo policzyć średnią dla każdego roku, za
# pomocą wzoru:
#
#   sum( rok ) / len( rok )
#
# gdzie rok to jest lista miesięcznych temperatur na naszej liście srednich.
# zaczynamy od pustej listy średnich, bo nie wiemy, ile będzie roczników 
# danych do przeanalizowania. 
roczniki = []

# i teraz dla każdego pomiaru na liście naszych danych
# sprawdzimy z jakiego roku są to dane i pogrupujemy temperatury
# w odpowiednie listy dla każdego roku
for pomiar in dane:
  # żeby nie używać głupich nazw z indeksami, nadamy sobie tymczasowe
  # nazwy dla wartości, które nas interesują: rok i temperatura
  rok  = pomiar[1]
  temp = pomiar[4]

  # tutaj robimy sprytny trick:
  #   1. sprawdzamy jaki jest pierwszy rocznik, czyli rok z pierwszego
  #      wiersza naszej tabeli. w naszym przypadku jest to rok 2009
  pierwszy_rok = dane[0][1]

  #   2. sprawdzamy, który w kolejności rocznik teraz przeglądamy,
  #      czyli np. jeśli jesteśmy w roczniku 2009 to wiemy, że to
  #      nasz pierwszy rocznik, bo pierwszy rok to 2009, czyli
  #
  #        2009 - 2009 + 1 --> 1
  #
  #      w następnym roczniku, czyli 2010 dostaniemy 2, bo
  #
  #        2010 - 2009 + 1 --> 2
  #
  #      i to się zgadza, bo 2010 to drugi rocznik w naszych danych
  aktualny_rocznik = rok - pierwszy_rok + 1

  #   3. jeśli długość listy roczniki jest mniejsza niż numer rocznika
  #      który przeglądamy (czyli, to co policzyliśmy powyżej) to 
  #      znaczy, że natrafiliśmy na pierwszy wiersz kolejnego rocznika
  #      i musimy stworzyć dla niego nową pustą listę na liście naszych
  #      roczników temperatur
  if len(roczniki) < aktualny_rocznik:
    roczniki.append([])

  #   4. do ostatniego rocznika na liście naszych roczników dodajmy
  #      aktualną temperaturę. dlaczego? bo ostatni rocznik jest 
  #      zawsze aktualny, dzięki temu co zrobiliśmy powyżej
  roczniki[-1].append(temp)

# liczymy średnie dla każdego rocznika. jak? lista roczników to
# lista list temperatur. każda lista na liście roczników to 
# temperatury miesięczne dla kolejnych lat (2009-2011). musimy
# zatem przejechać po tej liście roczników pętlą i dla każdego
# rocznika policzyć średnią temperaturę

# zaczynamy od wyjęcia z tabeli pierwszego rocznika, żebyśmy mogli
# ładnie wydrukować kolejne lata
aktualny_rok = dane[0][1]
# dla każdego rocznika (listy temperatur miesięcznych) na liście roczników
for rocznik in roczniki:
  # policz średnią temperaturę w danym roku
  srednia = sum(rocznik) / len(rocznik)

  # wydrukuj ładnie pamiętając, by zmienić liczby na napisy funkcją str
  print str(aktualny_rok) + ": " + str(srednia)

  # dodaj jeden do roku, by wyświetlić za chwilę następny rocznik
  aktualny_rok = aktualny_rok + 1


