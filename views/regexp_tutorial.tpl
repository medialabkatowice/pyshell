<br />

<div class="row">
  <div class="twelve columns">
    <h2 class="center">MediaLab → Miasto otwarte</h2>
  </div>
</div>


<div class="row">
  <div class="four columns"> </div>
  <div class="eight columns">
    <h4>Indeks cen żywności</h4>
  </div>
</div>

<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Standardowy CSV
    </p> </div>
    <div class="eight columns"> <p>
        W ustandaryzowanym pliku CSV wartości numeryczne nie powinny
        być objęte w dodatkowe cudzysłowy. Zmień to w pliku z indeksami
        cen żywności.
    </p> </div>
</div> </div>

<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Sortowalne daty
    </p> </div>
    <div class="eight columns"> <p>
        Daty w tym pliku nie dają się sortować. Gdybysmy to bowiem zrobili
        najpierw dostaniemy same stycznie, później same lute itd. Przestaw
        kolejność cząstek miesiąc i rok tak, by dane dało się łatwo posortować
        (najpierw rok, później miesiąc). Przy okazji zmień rzadki w Polsce
        ciach na kropkę. Ostatecznie każda data powinna przyjąć następującą
        postać: RRRR.MM (np.: 1990.01) 
    </p> </div>
</div> </div>

<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Roczne indeksy cen mięsa
    </p> </div>
    <div class="eight columns"> <p>
        Plik z indeksami cen żywności zawiera dane z każdego miesiąca
        roku. Stwórz nowy plik CSV zawierający tylko dwie kolumny: rok
        i indeks cen mięsa. Niech zebrane dane będą tylko indeksami
        styczniowymi. 
    </p> </div>
</div> </div>

<div class="row">
  <div class="four columns"> </div>
  <div class="eight columns">
    <h4>Edycje Wikipedii</h4>
  </div>
</div>


<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Dynamika zmian
    </p> </div>
    <div class="eight columns"> <p>
        Stwórz plik CSV zawierający godzinę, datę oraz wielkość
        artykułu. Pamiętaj o oddzieleniu kolumn średnikami i objęciu
        kolumn tekstowych w cudzysłów.
    </p> </div>
</div> </div>

<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Ujemne linki
    </p> </div>
    <div class="eight columns"> <p>
        Znajdź autorów edycji dotyczących linków w artykule, które
        zmiejszyły objętość tego artykułu.
    </p> </div>
</div> </div>




<div class="row">
  <div class="four columns"> </div>
  <div class="eight columns">
    <h4>Rejestr zabytków</h4>
  </div>
</div>


<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Data decyzji
    </p> </div>
    <div class="eight columns"> <p>
        Każdy obiekt w rejestrze zabytków posiada numer decyzji
        składający sie z abstrakcyjnego identyfikatora oraz daty,
        kiedy wpisu dokonano. Wydobąć daty roczne wszystkich wpisów do
        rejestru. UWAGA: niektóre obiekty maja kilka dat, bo rejestr
        był aktualizowany - wydobądź wszystkie te daty.
    </p> </div>
</div> </div>


<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Datowanie kościołów i kaplic
    </p> </div>
    <div class="eight columns"> <p>
        Wydobądź daty powstania wszystkich kościołów i kaplic w
        rejestrze zabytków. Wynik powinien zawierać zarówno nazwę
        obiektu, jak i datowanie.
    </p> </div>
</div> </div>


<div class="row spacer"> <div class="twelve columns">
    <div class="four columns"> <p class="right">
        Ostatnie datowania obiektów
    </p> </div>
    <div class="eight columns"> <p>
        Wiele obiektów w rejestrze ma wiele dat powstania (co związane
        jest z przebudowami, spaleniami itp). Wydobądź nazwy
        wszystkich obiektów wraz z ostanią informacją o datowaniu.
        Gdybyśmy chcieli to zrobić w sposób ścisły i dokładny, byłoby
        to zadanie bardzo trudne. Przyjmijmy zatem założenie, że
        chodzi o pełne roczniki lub wieki (czyli: jeśli jakiś obiekt
        posiada datowanie "XVII, 2poł. XIX", poza nazwą wystarczy
        wydobyć "XIX").
    </p> </div>
</div> </div>

%rebase base js=None
