# -*- coding: utf-8 -*-
"""
Licencja
"""

from sys import exit

# Stałe.
###############################################################################
ZNAK_ZACHETY = "> "

# Statystyki.
###############################################################################
ekwipunek = []
decyzje = {}

# Funkcje pomocnicze.
###############################################################################
def wybor(zakres=0, prompt=ZNAK_ZACHETY):
    """
    Funkcja przyjmująca komendy od użytkownika.
    """
    while True:
        liczba = raw_input(prompt)
        if liczba.isdigit():
            liczba = int(liczba)
            if liczba == 0:
                exit(0)
            elif liczba > zakres or liczba < 0:
                print u"Błąd! Zła liczba!"
            else:
                return liczba
        else:
            print u"Błąd! Musisz wpisać liczbę!"

# Interfejs.
###############################################################################
# Działa następująco:
# Najpierw definiujemy pierwszą funkcję przy pomocy dodaj_wywolanie.
# Następnie wywołujemy funkcję wywolywuj_funkcje.
# Wewnątrz pierwszej funkcji dodajemy wywołanie do kolejnej.
# Dzięki temu, gdy pierwsza się zakończy, jest uruchamiania druga.
# Jeśli żadna funkcja nie została zdefiniowana, to wywoływanie się kończy.

# Zmienne pomocnicze.
nastepna_funkcja = ""

def wykonaj(nazwa_funkcji):
    """Wykonuje funkcję nazwa_funkcji (string) i zwraca jej wynik."""
    return globals()[nazwa_funkcji]()

def wywolywuj_funkcje():
    """Wywołuje funkcje, dopóki jest zdefiniowana nastepna_funkcja."""
    global nastepna_funkcja
    while nastepna_funkcja != None:
        funkcja = nastepna_funkcja
        nastepna_funkcja = None
        wykonaj(funkcja)

def dodaj_wywolanie(nazwa_funkcji):
    """Po wykonaniu funkcji, w której ta została użyta, zostanie wykonana
    kolejna (podana w argumencie). Działa razem z wywolywuj_funkcje."""
    global nastepna_funkcja
    nastepna_funkcja = nazwa_funkcji

# Logika gry.
###############################################################################
def start():
    """Od tego zaczyna się gra."""
    reset()
    print (
        u"\nWitaj w grze \"Zakazany Las\"!\n\n"
        u"Przed Tobą czeka krótka przygoda, w której każda Twoja decyzja\n"
        u"będzie miała wpływ na dalszy bieg wydarzeń.\n"
        u"Przed każdą decyzją pojawi się krótka historyjka i lista\n"
        u"dostępnych, ponumerowanych decyzji. Wpisz liczbę reprezentującą\n"
        u"wybraną przez Ciebie decyzję i zatwierdź przyciskiem ENTER.\n\n"
        u"W grze nie ma żadnych zapisów i łatwo można zginąć, ale nic nie\n"
        u"stoi na przeszkodzie, aby zaczynać od nowa!\n\n"
        u"Życzę miłej zabawy!\n"
        u"Mateusz Przybył, autor tej gry\n\n"
        #u"Kod gry wydany na licencji GPLv3 na stronie github.com/zakazanylas\n\n"
        u"W każdej chwili możesz wpisać 0, aby wyjść.\n"
        u"1. Zacznij grę."
    )

    poczatek = wybor(1)

    print (
        u"\nJesteś podróżnikiem. Postanowiłeś przejść się na spacer,\n"
        u"jak zwykle po południu. Zmieniłeś tym razem drogę i zatrzymałeś\n"
        u"się na skraju lasu. Gęstwina drzew przed Tobą wygląda tajemniczo,\n"
        u"ale również interesująco.\n"
        u"1. Wejdź do lasu.\n"
        u"2. Wróć do domu."
    )
    poczatek = wybor(2)

    if poczatek == 1:
        dodaj_wywolanie("las")
    elif poczatek == 2:
        dodaj_wywolanie("dom")

def las():
    print (
        u"\nWchodzisz do lasu. Ciarki przeszły Cię po plecach.\n"
        u"Ścieżka wygląda na nieużywaną od lat. To źle wróży.\n"
        u"Jednak idziesz dalej, aż w końcu napotykasz na rozdroże.\n"
        u"Wtem słyszysz szelest dobiegający zza krzaków.\n"
        u"Może warto wrócić, póki nie jest za późno?\n"
        u"1. Idź w lewo.\n"
        u"2. Idź w prawo.\n"
        u"3. Sprawdź, co mogło wywołać szelest.\n"
        u"4. Zawróć."
    )

    dzialanie = wybor(4)

    if dzialanie == 1:
        dodaj_wywolanie("sciezka_w_lewo")
    elif dzialanie == 2:
        dodaj_wywolanie("sciezka_w_prawo")
    elif dzialanie == 3:
        dodaj_wywolanie("szelest")
    elif dzialanie == 4:
        dodaj_wywolanie("powrot")

def rozdroze():
    print (
        u"\nJesteś z powrotem na rozdrożu.\n"
        u"1. Idź w lewo.\n"
        u"2. Idź w prawo.\n"
        u"3. Sprawdź krzaki.\n"
        u"4. Zawróć."
    )
    dzialanie = wybor(4)

    if dzialanie == 1:
        dodaj_wywolanie("sciezka_w_lewo")
    elif dzialanie == 2:
        dodaj_wywolanie("sciezka_w_prawo")
    elif dzialanie == 3:
        dodaj_wywolanie("szelest")
    elif dzialanie == 4:
        dodaj_wywolanie("powrot")

def sciezka_w_lewo():
    global decyzje
    if decyzje["nora"] == True:
        print (
            u"\nZnowu spotykasz tajemniczego królika. Nie zamierzasz wracać\n"
            u"do króliczej nory, więc odwracasz się na pięcie i idziesz."
        )
        dodaj_wywolanie("rozdroze")
        return
    print (
        u"\nPo kilku minutach marszu zaczynasz odczuwać nudę. W pewnym momencie\n"
        u"zauważasz niewielkiego królika, który Tobie się przypatruje.\n"
        u"Postanawiasz się zatrzymać na chwilę i go pogłaskać. Jednak\n"
        u"jak tylko się zbliżasz, królik ucieka.\n"
        u"1. Goń królika.\n"
        u"2. Zawróć."
    )
    dzialanie = wybor(2)
    if dzialanie == 1:
        decyzje["nora"] = True
        dodaj_wywolanie("krolicza_nora_1")
    elif dzialanie == 2:
        dodaj_wywolanie("rozdroze")

def krolicza_nora_1():
    print (
        u"\nZ niewiadomego powodu odczuwasz potrzebę pogłaskania królika, więc\n"
        u"biegniesz za nim. Nagle tracisz grunt pod stopami i stwierdzasz, że\n"
        u"wpadłeś do dziury. Bardzo głębokiej dziury, bo spadasz, i spadasz,\n"
        u"i spadasz, i spadasz, i spadasz, i spadasz, i spadasz, i spadasz,\n"
        u"aż w końcu lądujesz w prawie pustym pokoju. Jesteś zdziwiony, bo\n"
        u"nie odczułeś w żaden sposób skutków upadku.\n\nPodchodzisz do "
        u"drewnianego stołu, na którym znajdują się trzy fiolki z płynami\n"
        u"o różnych kolorach. Dostrzegasz również pustą fiolkę wiszącą na\n"
        u"ścianie z napisem \"Wybieraj\".\n"
        u"1. Wlej zawartość fiolki z podpisem \"Szczęście\".\n"
        u"2. Wlej zawartość fiolki z podpisem \"Miłosierność\".\n"
        u"3. Wlej zawartość fiolki z podpisem \"Skromność\"."
    )
    fiolka = wybor(3)
    if fiolka == 2:
        print (
            u"\nWlewasz płyn do pustej fiolki i obserwujesz, jak ściana\n"
            u"wysuwa się odsłaniając kolejne pomieszczenie. Zadowolony\n"
            u"wchodzisz do środka."
        )
        dodaj_wywolanie("krolicza_nora_2")
    else:
        print (
            u"\nWlewasz płyn do pustej fiolki. Nic się nie dzieje. Czekasz\n"
            u"kilkanaście minut po czym zrezygnowany wylewasz zawartość\n"
            u"i wlewasz płyny z pozostałych fiolek. Żadna nie podziałała.\n"
            u"Zastanawiasz się, co dalej, przeszukujesz całe pomieszczenie,\n"
            u"ale nic nie znajdujesz. Wpadasz na pomysł, że być może musisz\n"
            u"wypić jeden z napojów. Bierzesz więc ten, który wybrałeś\n"
            u"na początku i pijesz do dna. Po chwili odczuwasz zawroty głowy\n"
            u"i upadasz. Zastanawiasz się, po co wszedłeś do zakazanego lasu?\n"
        )
        dodaj_wywolanie("przegrana")

def krolicza_nora_2():
    global decyzje
    global ekwipunek
    print (
        u"\nW kolejnym pokoju wita Cię piszczący z rozpaczy wilk zamknięty\n"
        u"w dużej klatce na środku pomieszczenia. Zauważasz na końcu pokoju\n"
        u"napis \"Wyjście\" i głęboką, wąską wyrwę obok. Na końcu dziury\n"
        u"dostrzegasz przycisk, ale nie jesteś w stanie przecisnąć ręki.\n"
        u"Znajdujesz w rogu kołek i idziesz w stronę drzwi, ale wilk\n"
        u"przypomina o sobie swoim piszczeniem. Wygląda na głodnego...\n"
        u"Otwierasz drzwi, ale ostatni raz spoglądasz się na uwięzionego\n"
        u"drapieżnika.\n"
        u"1. Wróć do rozdroża.\n"
        u"2. Najpierw uwolnij wilka."
    )
    ekwipunek.append("Kołek")
    dzialanie = wybor(2)
    if dzialanie == 1:
        print (
            u"\nWychodzisz z pomieszczenia, a zaraz za Tobą drzwi same się\n"
            u"zatrzaskują. Za nimi słyszysz głośno skomlącego wilka, a po chwili\n"
            u"strzał. Skomlenie ustało. Wilk nie żyje. Nie jesteś w stanie\n"
            u"otworzyć drzwi, więc biegniesz, ile sił w nogach, byle dalej\n"
            u"od tego przeklętego miejsca."
        )
        decyzje["pomoc"] = False
    elif dzialanie == 2:
        print (
            u"\nZamek okazał się prosty do złamania, więc otworzyłeś dzrzwiczki\n"
            u"od klatki. Wilk wybiegł z niej zadowolony i ustawił się w pozycji\n"
            u"jakby chciał skoczyć Tobie na głowę. Instyktownie przybrałeś postawę\n"
            u"obronną, ale zwierzę najwyraźniej się rozmyśliło i wybiegło przez \n"
            u"otwarte drzwi. Uspokajając się również wyszedłeś. Drzwi\n"
            u"zatrzasnęły się za Tobą, a wilka nie było słychać ani widać.\n"
            u"Zadowolony opuszczasz to przeklęte miejsce."
        )
    dodaj_wywolanie("rozdroze")

def sciezka_w_prawo():
    global decyzje
    global ekwipunek
    print (
        u"\nIdziesz ścieżką, aż w końcu napotykasz na rzekę. Po drugiej stronie\n"
        u"zauważasz dalszą część drogi, ale musisz znaleźć sposób, aby\n"
        u"przedostać się na drugą stronę.\n"
        u"1. Zwal drzewo.\n"
        u"2. Zawróć."
    )
    liczba_wyborow = 2
    if "Lina" in ekwipunek:
        print u"3. Użyj liny."
        liczba_wyborow = 3
    dzialanie = wybor(liczba_wyborow)
    if dzialanie == 1:
        decyzje["rzeka_drzewo"] = True
        print (
            u"\nZauważasz dosyć mocno ścięte drzewo. Postanawiasz je wykorzystać\n"
            u"i do niego podchodzisz. Używasz całej swojej siły, aby je zwalić\n"
            u"w kierunku rzeki. Udało Ci się! W dodatku okazało się, że jest\n"
            u"dostatecznie wysokie i uczepiło się drugiego brzegu. Możesz\n"
            u"teraz po nim przejść na drugą stronę, co z dumą wykonujesz.\n"
            u"Zaraz po Twoim przejściu, zwalony pień porywa zwiększony\n"
            u"prąd rzeki.\n"
        )
        dodaj_wywolanie("za_rzeka")
    elif dzialanie == 2:
        print (
            u"\nStwierdzasz, że nie musisz (przynajmniej na razie) przechodzić\n"
            u"na drugą stronę, więc zawracasz."
        )
        dodaj_wywolanie("rozdroze")
    elif dzialanie == 3:
        print (
            u"\nDostrzegasz na drugim brzegu przybity kołek, o który\n"
            u"z powodzeniem mógłbyś zaczepić linę rzucająć jej pętelką zawiązaną\n"
            u"na końcu. Brakuje Ci jedynie czegoś, do czego mógłbyś ją przywiązać.\n"
            u"Lina jest za krótka, aby można było ją obwiązać wokół drzewa."
        )
        if "Kołek" not in ekwipunek:
            print (
                u"Rezygnujesz więc pomysłu przepłynięcia przez rwącą rzekę\n"
                u"trzymając się liny i wracasz do rozdroża."
            )
            dodaj_wywolanie("rozdroze")
        else:
            print (
                u"\nPrzypominasz sobie nagle o kołku z nory, który zachowałeś.\n"
                u"Wbijasz go w ziemię. Rzucasz liną na drugi brzeg. Trafiłeś\n"
                u"idealnie w kołek! Drugi koniec zahaczasz o swój i przepływasz\n"
                u"przez rzekę trzymając się kurczowo liny.\n"
                u"Udaje Ci się dotrzeć na drugi brzeg. Chociaż jesteś całkowicie\n"
                u"przemoczony, odczuwasz zadowolenie. Wziąłeś linę i zauważyłeś,\n"
                u"że mało brakowało do jej rozerwania. Nie wrócisz na drugi brzeg.\n"
            )
            dodaj_wywolanie("za_rzeka")

def za_rzeka():
    print (
        u"\nMimo braku możliwości powrotu idziesz hardo ścieżką. Na jej końcu\n"
        u"znajdujesz niewielką, drewnianą chatkę.\n"
        u"1. Wejdź do chatki.\n"
        u"2. Zawróć."
    )
    while True:
        dzialanie = wybor(2)
        if dzialanie == 1:
            dodaj_wywolanie("wiedzma")
            return
        elif dzialanie == 2:
            print u"\nNie ma sensu wracać!"

def wiedzma():
    global decyzje
    global ekwipunek
    bilans = 0
    licznik_klamstw = 0
    print (
        u"\nWchodzisz do chatki, a przed Tobą pojawia się stara kobieta o siwych\n"
        u"włosach."
    )
    # Pytanie pierwsze: jedzenie
    jedzenie = None
    if "Jedzenie" in ekwipunek:
        print (
            u"\n- Nie jadłam nic od tygodni, mógłbyś mi dać swoje jedzenie?\n"
            u"Byłeś zaskoczony jej wiedzą na temat Twoich jagódek.\n"
            u"1. Daj jej jedzenie.\n"
            u"2. Powiedz, że nie masz jedzenia."
        )
        dzialanie = wybor(2)
        if dzialanie == 1:
            jedzenie = True
        else:
            jedzenie = False
    if jedzenie != None:
        if jedzenie == True:
            print (
                u"\n- Jesteś hojnym człowiekiem! Zostaw sobie to jedzenie."
            )
            bilans += 1
        else:
            print (
                u"\n- Nie chcesz dzielić się z bliźnim? Niech tak będzie!"
            )
            bilans -= 1
    #print ("licznik_klamstw =", licznik_klamstw)
    #print ("bilans =", bilans)
    # Pytania moralne
    print (
        u"\nPodrapała się po głowie i powiedziała:\n"
        u"- Nie powinieneś był wchodzić do zakazanego lasu. Należy czytać znaki.\n"
        u"Masz szczęście, że doszedłeś tu do mnie. Pomogę Ci, ale najpierw\n"
        u"odpowiedz mi na kilka pytań, od których zależy, jak się skończy\n"
        u"twa podróż. Nie próbuj żadnych sztuczek, bo jestem w stanie\n"
        u"Cię zabić jednym machnięciem ręki.\n\n"
        u"Zaprezentowała to machając ręką i niszcząc wazon stojący na stole.\n"
    )
    # Pytanie drugie: przejście przez rzekę
    print (
        u"- Na początek chciałabym się dowiedzieć, jak przeszedłeś przez rzekę?\n"
        u"1. \"Zwaliłem drzewo.\"\n"
        u"2. \"Przepłynąłem. Nie widać?\""
    )
    odpowiedz = wybor(2)
    rzeka_drzewo = False
    if odpowiedz == 1:
        rzeka_drzewo = True
    if decyzje["rzeka_drzewo"]:
        bilans -= 1
    else:
        bilans += 1
    if rzeka_drzewo != decyzje["rzeka_drzewo"]:
        licznik_klamstw += 1
    #print ("licznik_klamstw =", licznik_klamstw)
    #print ("bilans =", bilans)
    # Pytanie trzecie: zabójstwo
    print (
        u"- Załóżmy, że Ci wierzę. Kolejne pytanie: czy zabiłeś kiedyś\n"
        u"żywe stworzenie?\n"
        u"1. \"Tak.\"\n"
        u"2. \"Nie.\""
    )
    odpowiedz = wybor(2)
    zabojstwo = False
    if odpowiedz == 1:
        zabojstwo = True
    if not (decyzje["wilk"] and decyzje["pomoc"]):
        bilans -= 1
    else:
        bilans += 1
    if zabojstwo != (not (decyzje["wilk"] and decyzje["pomoc"])):
        licznik_klamstw += 1
    #print ("licznik_klamstw =", licznik_klamstw)
    #print ("bilans =", bilans)
    # Pytanie czwarte: miłosierność
    print (
        u"- Czasami nie mamy wyboru, ale gdy go mamy, to często nie\n"
        u"wykorzystujemy go dobrze... Następne pytanie! Czy pomogłeś\n"
        u"kiedyś jakiemuś stworzeniu b e z i n t e r e s o w n i e ?\n"
        u"1. \"Tak.\"\n"
        u"2. \"Nie.\""
    )
    odpowiedz = wybor(2)
    milosiernosc = False
    if odpowiedz == 1:
        milosiernosc = True
    if decyzje["nora"] and decyzje["pomoc"]:
        bilans += 1
    elif decyzje["nora"]:
        bilans -= 1
    if decyzje["nora"] and milosiernosc != decyzje["pomoc"]:
        licznik_klamstw += 1
    #print ("licznik_klamstw =", licznik_klamstw)
    #print ("bilans =", bilans)
    # Pytanie dodatkowe [Colobot - easter egg]
    print (
        u"- Należy być miłosiernym dla bliźniego, nawet największego wroga!\n"
        u"Ostatnie pytanie: czy widziałeś gdzieś może pewną przerośniętą,\n"
        u"zieloną mrówkę? Zgubiła mi się...\n"
        u"1. \"Tak.\"\n"
        u"2. \"Nie.\""
    )
    odpowiedz = wybor(2)
    print (
        u"- To bez znaczenia!\n"
        u"Wiedźma zamyśliła się...\n"
    )
    # Podsumowanie
    if licznik_klamstw == 0:
        print u"- Nie okłamałeś mnie..."
    else:
        print u"- Coś kręcisz..."
    if jedzenie != None:
        if jedzenie:
            print u"- Chciałeś podarować mi jedzenie..."
        else:
            print u"- Pożałowałeś mi jedzenia..."
    if decyzje["rzeka_drzewo"]:
        print u"- Zniszczyłeś naturę..."
    else:
        print u"- Szanujesz naturę..."
    if not (decyzje["wilk"] and decyzje["pomoc"]):
        print u"- Zabiłeś żywe stworzenie..."
    else:
        print u"- Nie dokonałeś nigdy zabójstwa..."
    if decyzje["nora"] and decyzje["pomoc"]:
        print u"- Pomogłeś bliźniemu..."
    elif decyzje["nora"]:
        print u"- Zignorowałeś bliźniego w potrzebie..."
    bilans -= licznik_klamstw
    #print ("licznik_klamstw =", licznik_klamstw)
    #print ("bilans =", bilans)
    if bilans < 0:
        print (
            u"- Być może działałeś zgodnie ze swoim sumieniem, ale to za mało!\n"
            u"Obawiam się, że nie mogę Cię wypuścić z tego lasu.\n\n"
            u"Wiedźma machnęła ręką i nagle poczułeś, jak Twoje ciało drętwieje.\n"
            u"Po co wchodziłeś do zakazanego lasu?\n"
        )
        dodaj_wywolanie("przegrana")
    else:
        print (
            u"- Dobrze! Niech Ci będzie, pozwolę Ci wrócić, ale muszę użyć magii,\n"
            u"która bywa kapryśna. Mnie przekonałeś, przekonaj teraz naturę!\n"
            u"Oto jej zagadka:\n\n"
            u"P i e r w s z e to w wyścigu ostatniemu mówiono kierowcy,\n"
            u"D r u g i e to drugie pół składnika szkieletu.\n"
            u"1. \"Ostatni Trup?\"\n"
            u"2. \"Samochód?\"\n"
            u"3. \"Wolność?\"\n"
            u"4. \"Patrz na drogę, bo umrzesz?\"\n"
            u"5. \"Prawo?\""
        )
        odpowiedz = wybor(5)
        if odpowiedz == 3:
            print (
                u"Nagle poczułeś, jakby coś Cię wyrzuciło w powietrze\n"
                u"i zaczęło Ci się kręcić w głowie, aż w końcu straciłeś\n"
                u"przytomność. Obudziłeś się pomiędzy wejściem do\n"
                u"Zakazanego Lasu a swoim domem. To było ciekawe\n"
                u"przeżycie...\n"
            )
            dodaj_wywolanie("wygrana")
        else:
            print (
                u"Wiedźma posępniała.\n"
                u"- To zła odpowiedź... Twoj szczątki będą spoczywały w tym\n"
                u"lesie. Przykro mi!\n\n"
                u"Machnęła ręką."
            )
            dodaj_wywolanie("przegrana")

def szelest():
    global decyzje
    if decyzje["szelest"]:
        print (
            u"\nZmierzasz w stronę krzaków, w której spotkałeś wilka, ale szybko\n"
            u"stwierdzasz, że nie powinieneś tam iść drugi raz."
        )
        dodaj_wywolanie("rozdroze")
    else:
        decyzje["szelest"] = True
        print (
            u"\nPodchodzisz ostrożnie do krzaków, z których wydobył się tajemniczy szelest.\n"
            u"Upewniając się, że nic Ci nie grozi, przekraczasz je i odkrywasz, że\n"
            u"w tym miejscu został ślad po dawnej drodze. Uradowany z powodu odkrycia\n"
            u"i zaciekawiony podążasz nią dalej. Po kilku minutach zacząłeś się\n"
            u"zastanawiać, czy aby na pewno jesteś jeszcze na drodze. Doszedłeś\n"
            u"do wniosku, że nie. Zdezorientowany nie możesz znaleźć drogi powrotnej.\n"
            u"Zgubiłeś się.\n"
            u"Jednak nie masz wyboru, nie możesz tu zostać. Zauważasz mech rosnący na\n"
            u"drzewie, który wskazuje północ. W którym kierunku iść?\n"
            u"1. Północ. Drzewa wydają Ci się trochę inne niż pozostałe...\n"
            u"2. Wschód. Słychać stamtąd dźwięki, jakby jakieś zwierzę coś jadło.\n"
            u"3. Południe. Wydobywa się stamtąd dziwny zapach.\n"
            u"4. Zachód. Również coś czujesz w nozdrzach..."
        )
        dzialanie = wybor(4)

        if dzialanie == 1:
            dodaj_wywolanie("szelest_polnoc")
        elif dzialanie == 2:
            dodaj_wywolanie("szelest_wschod")
        elif dzialanie == 3:
            dodaj_wywolanie("szelest_poludnie")
        elif dzialanie == 4:
            dodaj_wywolanie("szelest_zachod")

def szelest_hub():
    global decyzje
    print (
        u"\nPoznajesz miejsce, w którym się znalazłeś. Patrzysz na mech\n"
        u"i decydujesz się pójść tym razem w inną stronę.\n"
        u"1. Północ. Drzewa wydają Ci się trochę inne niż pozostałe...\n"
        u"2. Wschód. Słychać stamtąd dźwięki, jakby jakieś zwierzę coś jadło.\n"
        u"3. Południe. Wydobywa się stamtąd dziwny zapach.\n"
        u"4. Zachód. Również coś czujesz w nozdrzach..."
    )
    while True:
        dzialanie = wybor(4)
        if dzialanie == 1 and not decyzje["szelest_polnoc"]:
            dodaj_wywolanie("szelest_polnoc")
            return
        elif dzialanie == 2 and not decyzje["szelest_wschod"]:
            dodaj_wywolanie("szelest_wschod")
            return
        elif dzialanie == 3 and not decyzje["szelest_poludnie"]:
            dodaj_wywolanie("szelest_poludnie")
            return
        elif dzialanie == 4 and not decyzje["szelest_zachod"]:
            dodaj_wywolanie("szelest_zachod")
            return
        else:
            print u"Już tam byłeś!"

def szelest_polnoc():
    global decyzje
    decyzje["szelest_polnoc"] = True
    print (
        u"\nPostanowiłeś ruszyć na północ. Idziesz ostrożnie deptając\n"
        u"po gałęziach. Nagle słyszysz głośny trzask i ogromny ból w nodze.\n"
        u"Z przerażeniem obserwujesz, jak pułapka zakleszczyła się\n"
        u"na Twojej nodze. Upadasz i zwijasz się z bólu. Słyszysz zmierzające\n"
        u"w Twoim kierunku wilki, które zwabił zapach krwi. Przypatrują się\n"
        u"Tobie, ich kolejnej ofiarze. Już wiesz, że to się źle skończy.\n"
        u"Jeden z wilków rzuca się do Twojego gardła i już nawet nie próbujesz\n"
        u"się bronić. Po co poszedłeś do tego zakazengo lasu?\n"
    )
    dodaj_wywolanie("przegrana")

def szelest_wschod():
    global decyzje
    global ekwipunek
    decyzje["szelest_wschod"] = True
    print (
        u"Im bardziej zbliżasz się do źródła niepokojących dźwięków,\n"
        u"tym bardziej Twój strach się nasila. Po pewnym czasie dostrzegasz\n"
        u"zwłoki sarny, którymi zajadał się wilk. Wstrzymujesz oddech\n"
        u"i cofasz się, ale niechcący łamiesz gałązkę, przez co drapieżnik\n"
        u"Cię zauważa. Zaczynasz uciekać w niewiadomym kierunku.\n"
        u"Wydaje Ci się, że trwało to wieczność, ale jakimś cudem trafiłeś\n"
        u"do znajomego rozdroża. Zatrzymujesz się i oglądasz się za siebie,\n"
        u"aby sprawdzić, czy wilk biegnie za Tobą. Niestety tak!\n"
    )
    if "Broń" not in ekwipunek and "Jedzenie" not in ekwipunek:
        print (
            u"Jesteś zbyt wycieńczony biegiem, by dalej uciekać. Czekasz, aż\n"
            u"drapieżnik się zbliży i liczysz na to, że uda Ci się wykorzystać\n"
            u"szansę i się obronić. Wilk skacze na Ciebie i dopada do gardła.\n"
            u"Mimo wszelkich wysiłków, nie udaje Ci się go odepchnąć.\n"
            u"Po co wszedłeś do zakazanego lasu?\n"
        )
        dodaj_wywolanie("przegrana")
    elif "Broń" in ekwipunek:
        print (
            u"Jesteś zbyt wycieńczony biegiem, by dalej uciekać. Czekasz, aż\n"
            u"drapieżnik się zbliży i liczysz na to, że uda Ci się wykorzystać\n"
            u"szansę i obronić się.\n"
            u"Przypominasz sobie o nożu, który znalazłeś. Wydobywasz go z kieszeni.\n"
            u"Wilk skacze na Ciebie, a Ty machasz nożem na oślep. Czujesz opór.\n"
            u"Otwierasz oczy i widzisz wykrwawiające się zwierzę.\n"
            u"Po co wszedłeś do zakazanego lasu?\n"
            u"Czekasz, aż wilk przestanie się ruszać. Chowasz jego ciało za krzakami."
        )
        decyzje["wilk"] = False
        dodaj_wywolanie("rozdroze")
    elif "Jedzenie" in ekwipunek:
        print (
            u"Nie zastanawiając się długo, postanawiasz rzucić się do dalszej\n"
            u"ucieczki. Nie masz pojęcia, jaką ścieżkę wybrałeś, ale biegniesz.\n"
            u"Nagle widzisz przed sobą rzekę i zaczynasz myśleć, że wszystko stracone.\n"
            u"Jednak oglądasz się za siebie i widzisz, że wilk już Cię nie goni.\n"
            u"Uradowany poisz się wodą z rzeki po czym wracasz ścieżką."
        )
        decyzje["wilk"] = True
        dodaj_wywolanie("rozdroze")

def szelest_poludnie():
    global decyzje
    global ekwipunek
    decyzje["szelest_poludnie"] = True
    print (
        u"\nNiewiele kroków musiałeś przejść, aby dostrzec, skąd wydobywa\n"
        u"się nieprzyjemny zapach. Na ziemi leżą zwłoki, szkielet człowieka.\n"
        u"Odruchowo zatykasz nos i cofasz się, ale po chwili podchodzisz,\n"
        u"aby sprawdzić, czy nie ma tu przypadkiem czegoś przydatnego.\n"
        u"Poza długim i dosyć ostrym nożem i liną nie znajdujesz nic godnego uwagi.\n"
        u"Bierzesz go ze sobą, razem z długą liną."
    )
    ekwipunek.append("Broń")
    ekwipunek.append("Lina")
    dodaj_wywolanie("szelest_hub")

def szelest_zachod():
    global decyzje
    global ekwipunek
    decyzje["szelest_zachod"] = True
    print (
        u"\nRuszasz w kierunku krzaków na zachodzie. Po kilku sekundach\n"
        u"z niedowierzaniem dostrzegasz rosnące jagody. Nagle przypomniało\n"
        u"Ci się, że jesteś głodny, więc zacząłeś jeść. Odczułeś przypływ\n"
        u"energii i wiary w siebie. Bierzesz trochę na drogę.\n"
        u"Zgubiłeś kierunek, ale idziesz dalej."
    )
    ekwipunek.append("Jedzenie")
    dodaj_wywolanie("szelest_hub")

def powrot():
    global decyzje
    if not decyzje["drzewo"]:
        print (
            u"\nOdwracasz się na pięcie i idziesz wydeptaną wcześniej przez siebie\n"
            u"ścieżką. Nagle, niespodziewanie upada przed Tobą drzewo.\n"
            u"Wystraszony cofasz się i postanawiasz obejść przeszkodę idąc\n"
            u"na około, ale gdy tylko zbliżasz się do krawędzi ścieżki,\n"
            u"zaczynasz słyszeć ciężkie dyszenie i warczenie.\n"
            u"Lepiej poszukać innej drogi."
        )
        decyzje["drzewo"] = True
    else:
        print (
            u"\nIdziesz w stronę zawalonego drzewa. Już z oddali widzisz, że\n"
            u"nic się nie zmieniło. Próbujesz obejść przeszkodę, ale\n"
            u"niebezpieczeństwo czające się za ścieżką jest zbyt przerażające.\n"
            u"Zdenerwowany wracasz do rozdroża."
        )

    dodaj_wywolanie("rozdroze")

def dom():
    print (
        u"Wracasz do domu. Nie masz ochoty na żadne przygody."
    )
    dodaj_wywolanie("wygrana")

def wygrana():
    print (
        u"\n\n"
        u"Gratulacje! Wygrałeś! Chcesz spróbować jeszcze raz?\n"
        u"1. Tak.\n"
        u"2. Nie."
    )
    jeszcze_raz = wybor(2)

    if jeszcze_raz == 1:
        print u"Doskonale! Może odkryjesz coś nowego...\n"
        dodaj_wywolanie("start")
    elif jeszcze_raz == 2:
        exit(0)

def przegrana():
    print (
        u"Zginąłeś. Chcesz spróbować jeszcze raz?\n"
        u"1. Tak.\n"
        u"2. Nie."
    )
    jeszcze_raz = wybor(2)

    if jeszcze_raz == 1:
        print u"Doskonale! Nie poddajesz się! Może odkryjesz coś nowego...\n"
        dodaj_wywolanie("start")
    elif jeszcze_raz == 2:
        exit(0)

def reset():
    global ekwipunek
    global decyzje

    # Broń, Lina, Jedzenie, Kołek
    ekwipunek = []

    decyzje = {
        "drzewo": False,
        "szelest": False,
        "szelest_polnoc": False,
        "szelest_wschod": False,
        "szelest_zachod": False,
        "szelest_poludnie": False,
        "wilk": True, # zyje
        "nora": False,
        "pomoc": True, # zyje
        "rzeka_drzewo": False,
    }

###############################################################################

if __name__ == "__main__":
    dodaj_wywolanie("start")
    wywolywuj_funkcje()