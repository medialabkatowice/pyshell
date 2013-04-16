# -*- coding: utf-8 -*-
# jakie zabawki mamy na półeczce?
zabawki = ["Miś", "Kotek", "Krokodyl"]

# zaczynamy zabawę
print "- Marysiu, przyniesiesz mi zabawki z półeczki?"

# zabawka po zabawce Marysia będzie tuptała
# do półeczki aż do wyczerpania zapasów
for maskotka in zabawki:
    print "- Taaaaaak!"
    # zrobimy mały odstęp, żeby łatwiej było czytać wyniki
    print ""
    
    print "Marysia tupi tupi do półeczki"
    print "Marysia patrzy a tam " + maskotka
    print "Marysia bierze maskotkę i tpi tupi do tatusia"
    print "- Malysia przyniosła to. " + maskotka
    print "- Dziękuję. Są jeszcze inne zabawki?"

# nawet Marysia wie, że...
print "- Nieee."
print "- Czyli na półeczce były " + ", ".join(zabawki)
print "- Malysia chce jeszcze!"

