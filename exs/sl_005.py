# lista zabawek do zabawy
zabawki = ["Miś", "Kotek", "Lisek", "Krokodyl"]

# dla każdej maskotki wśród tych zabawek
for maskotka in zabawki:
    print "- Proszę, oto zabawka"

    # jeśli nazwa tej maskotki zaczyna się od 'K', cieszymy się!
    if maskotka.startswith('K'):
        print "- Hurra: " + maskotka

    # w przeciwnym razie, jeśli (elif) nazwa zaczyna się od 'M', jest ok.
    elif maskotka.startswith('M'):
        print "- " + maskotka + ", niech będzie..."

    # w przeciwnym razie (else) nie podoba nam się taka maskotka
    else:
        print "- Łeeeee to tylko " + maskotka

    print "- Chcesz następną?"
    print "- Tak!"
    
print "- No i koniec!"
