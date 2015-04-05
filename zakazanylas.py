# -*- coding: utf-8 -*-
"""
Autor: Mateusz "Simbax" Przybyl
Licencja: GPLv3 
Python: 2.7
Strona: github.com/MrSimbax/Zakazany-Las
"""

from sys import exit

# Stale.
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
    Funkcja przyjmujaca komendy od uzytkownika.
    """
    while True:
        liczba = raw_input(prompt)
        if liczba.isdigit():
            liczba = int(liczba)
            if liczba == 0:
                exit(0)
            elif liczba > zakres or liczba < 0:
                print u"Blad! Zla liczba!"
            else:
                return liczba
        else:
            print u"Blad! Musisz wpisac liczbe!"

# Interfejs.
###############################################################################
# Dziala nastepujaco:
# Najpierw definiujemy pierwsza funkcje przy pomocy dodaj_wywolanie.
# Nastepnie wywolujemy funkcje wywolywuj_funkcje.
# Wewnatrz pierwszej funkcji dodajemy wywolanie do kolejnej.
# Dzieki temu, gdy pierwsza sie zakonczy, jest uruchamiania druga.
# Jesli zadna funkcja nie zostala zdefiniowana, to wywolywanie sie konczy.

# Zmienne pomocnicze.
nastepna_funkcja = ""

def wykonaj(nazwa_funkcji):
    """Wykonuje funkcje nazwa_funkcji (string) i zwraca jej wynik."""
    return globals()[nazwa_funkcji]()

def wywolywuj_funkcje():
    """Wywoluje funkcje, dopoki jest zdefiniowana nastepna_funkcja."""
    global nastepna_funkcja
    while nastepna_funkcja != None:
        funkcja = nastepna_funkcja
        nastepna_funkcja = None
        wykonaj(funkcja)

def dodaj_wywolanie(nazwa_funkcji):
    """Po wykonaniu funkcji, w ktorej ta zostala uzyta, zostanie wykonana
    kolejna (podana w argumencie). Dziala razem z wywolywuj_funkcje."""
    global nastepna_funkcja
    nastepna_funkcja = nazwa_funkcji

# Logika gry.
###############################################################################
def start():
    """Od tego zaczyna sie gra."""
    reset()
    print (
        u"\nWitaj w grze \"Zakazany Las\"!\n\n"
        u"Przed Toba czeka krotka przygoda, w ktorej kazda Twoja decyzja\n"
        u"bedzie miala wplyw na dalszy bieg wydarzen.\n"
        u"Przed kazda decyzja pojawi sie krotka historyjka i lista\n"
        u"dostepnych, ponumerowanych decyzji. Wpisz liczbe reprezentujaca\n"
        u"wybrana przez Ciebie decyzje i zatwierdz przyciskiem ENTER.\n\n"
        u"W grze nie ma zadnych zapisow i latwo mozna zginac, ale nic nie\n"
        u"stoi na przeszkodzie, aby zaczynac od nowa!\n\n"
        u"zycze milej zabawy!\n"
        u"Mateusz Przybyl, autor tej gry\n\n"
        u"Kod gry zostal wydany na licencji GPLv3 na stronie\n"
        u"github.com/MrSimbax/Zakazany-Las\n\n"
        u"W kazdej chwili mozesz wpisac 0, aby wyjsc.\n"
        u"1. Zacznij gre."
    )

    poczatek = wybor(1)

    print (
        u"\nJestes podroznikiem. Postanowiles przejsc sie na spacer,\n"
        u"jak zwykle po poludniu. Zmieniles tym razem droge i zatrzymales\n"
        u"sie na skraju lasu. Gestwina drzew przed Toba wyglada tajemniczo,\n"
        u"ale rowniez interesujaco.\n"
        u"1. Wejdz do lasu.\n"
        u"2. Wroc do domu."
    )
    poczatek = wybor(2)

    if poczatek == 1:
        dodaj_wywolanie("las")
    elif poczatek == 2:
        dodaj_wywolanie("dom")

def las():
    print (
        u"\nWchodzisz do lasu. Ciarki przeszly Cie po plecach.\n"
        u"sciezka wyglada na nieuzywana od lat. To zle wrozy.\n"
        u"Jednak idziesz dalej, az w koncu napotykasz na rozdroze.\n"
        u"Wtem slyszysz szelest dobiegajacy zza krzakow.\n"
        u"Moze warto wrocic, poki nie jest za pozno?\n"
        u"1. Idz w lewo.\n"
        u"2. Idz w prawo.\n"
        u"3. Sprawdz, co moglo wywolac szelest.\n"
        u"4. Zawroc."
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
        u"\nJestes z powrotem na rozdrozu.\n"
        u"1. Idz w lewo.\n"
        u"2. Idz w prawo.\n"
        u"3. Sprawdz krzaki.\n"
        u"4. Zawroc."
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
            u"\nZnowu spotykasz tajemniczego krolika. Nie zamierzasz wracac\n"
            u"do kroliczej nory, wiec odwracasz sie na piecie i idziesz."
        )
        dodaj_wywolanie("rozdroze")
        return
    print (
        u"\nPo kilku minutach marszu zaczynasz odczuwac nude. W pewnym momencie\n"
        u"zauwazasz niewielkiego krolika, ktory Tobie sie przypatruje.\n"
        u"Postanawiasz sie zatrzymac na chwile i go poglaskac. Jednak\n"
        u"jak tylko sie zblizasz, krolik ucieka.\n"
        u"1. Gon krolika.\n"
        u"2. Zawroc."
    )
    dzialanie = wybor(2)
    if dzialanie == 1:
        decyzje["nora"] = True
        dodaj_wywolanie("krolicza_nora_1")
    elif dzialanie == 2:
        dodaj_wywolanie("rozdroze")

def krolicza_nora_1():
    print (
        u"\nZ niewiadomego powodu odczuwasz potrzebe poglaskania krolika, wiec\n"
        u"biegniesz za nim. Nagle tracisz grunt pod stopami i stwierdzasz, ze\n"
        u"wpadles do dziury. Bardzo glebokiej dziury, bo spadasz, i spadasz,\n"
        u"i spadasz, i spadasz, i spadasz, i spadasz, i spadasz, i spadasz,\n"
        u"az w koncu ladujesz w prawie pustym pokoju. Jestes zdziwiony, bo\n"
        u"nie odczules w zaden sposob skutkow upadku.\n\nPodchodzisz do "
        u"drewnianego stolu, na ktorym znajduja sie trzy fiolki z plynami\n"
        u"o roznych kolorach. Dostrzegasz rowniez pusta fiolke wiszaca na\n"
        u"scianie z napisem \"Wybieraj\".\n"
        u"1. Wlej zawartosc fiolki z podpisem \"Szczescie\".\n"
        u"2. Wlej zawartosc fiolki z podpisem \"Milosiernosc\".\n"
        u"3. Wlej zawartosc fiolki z podpisem \"Skromnosc\"."
    )
    fiolka = wybor(3)
    if fiolka == 2:
        print (
            u"\nWlewasz plyn do pustej fiolki i obserwujesz, jak sciana\n"
            u"wysuwa sie odslaniajac kolejne pomieszczenie. Zadowolony\n"
            u"wchodzisz do srodka."
        )
        dodaj_wywolanie("krolicza_nora_2")
    else:
        print (
            u"\nWlewasz plyn do pustej fiolki. Nic sie nie dzieje. Czekasz\n"
            u"kilkanascie minut po czym zrezygnowany wylewasz zawartosc\n"
            u"i wlewasz plyny z pozostalych fiolek. zadna nie podzialala.\n"
            u"Zastanawiasz sie, co dalej, przeszukujesz cale pomieszczenie,\n"
            u"ale nic nie znajdujesz. Wpadasz na pomysl, ze byc moze musisz\n"
            u"wypic jeden z napojow. Bierzesz wiec ten, ktory wybrales\n"
            u"na poczatku i pijesz do dna. Po chwili odczuwasz zawroty glowy\n"
            u"i upadasz. Zastanawiasz sie, po co wszedles do zakazanego lasu?\n"
        )
        dodaj_wywolanie("przegrana")

def krolicza_nora_2():
    global decyzje
    global ekwipunek
    print (
        u"\nW kolejnym pokoju wita Cie piszczacy z rozpaczy wilk zamkniety\n"
        u"w duzej klatce na srodku pomieszczenia. Zauwazasz na koncu pokoju\n"
        u"napis \"Wyjscie\" i gleboka, waska wyrwe obok. Na koncu dziury\n"
        u"dostrzegasz przycisk, ale nie jestes w stanie przecisnac reki.\n"
        u"Znajdujesz w rogu kolek i idziesz w strone drzwi, ale wilk\n"
        u"przypomina o sobie swoim piszczeniem. Wyglada na glodnego...\n"
        u"Otwierasz drzwi, ale ostatni raz spogladasz sie na uwiezionego\n"
        u"drapieznika.\n"
        u"1. Wroc do rozdroza.\n"
        u"2. Najpierw uwolnij wilka."
    )
    ekwipunek.append("Kolek")
    dzialanie = wybor(2)
    if dzialanie == 1:
        print (
            u"\nWychodzisz z pomieszczenia, a zaraz za Toba drzwi same sie\n"
            u"zatrzaskuja. Za nimi slyszysz glosno skomlacego wilka, a po chwili\n"
            u"strzal. Skomlenie ustalo. Wilk nie zyje. Nie jestes w stanie\n"
            u"otworzyc drzwi, wiec biegniesz, ile sil w nogach, byle dalej\n"
            u"od tego przekletego miejsca."
        )
        decyzje["pomoc"] = False
    elif dzialanie == 2:
        print (
            u"\nZamek okazal sie prosty do zlamania, wiec otworzyles dzrzwiczki\n"
            u"od klatki. Wilk wybiegl z niej zadowolony i ustawil sie w pozycji\n"
            u"jakby chcial skoczyc Tobie na glowe. Instyktownie przybrales postawe\n"
            u"obronna, ale zwierze najwyrazniej sie rozmyslilo i wybieglo przez \n"
            u"otwarte drzwi. Uspokajajac sie rowniez wyszedles. Drzwi\n"
            u"zatrzasnely sie za Toba, a wilka nie bylo slychac ani widac.\n"
            u"Zadowolony opuszczasz to przeklete miejsce."
        )
    dodaj_wywolanie("rozdroze")

def sciezka_w_prawo():
    global decyzje
    global ekwipunek
    print (
        u"\nIdziesz sciezka, az w koncu napotykasz na rzeke. Po drugiej stronie\n"
        u"zauwazasz dalsza czesc drogi, ale musisz znalezc sposob, aby\n"
        u"przedostac sie na druga strone.\n"
        u"1. Zwal drzewo.\n"
        u"2. Zawroc."
    )
    liczba_wyborow = 2
    if "Lina" in ekwipunek:
        print u"3. Uzyj liny."
        liczba_wyborow = 3
    dzialanie = wybor(liczba_wyborow)
    if dzialanie == 1:
        decyzje["rzeka_drzewo"] = True
        print (
            u"\nZauwazasz dosyc mocno sciete drzewo. Postanawiasz je wykorzystac\n"
            u"i do niego podchodzisz. Uzywasz calej swojej sily, aby je zwalic\n"
            u"w kierunku rzeki. Udalo Ci sie! W dodatku okazalo sie, ze jest\n"
            u"dostatecznie wysokie i uczepilo sie drugiego brzegu. Mozesz\n"
            u"teraz po nim przejsc na druga strone, co z duma wykonujesz.\n"
            u"Zaraz po Twoim przejsciu, zwalony pien porywa zwiekszony\n"
            u"prad rzeki.\n"
        )
        dodaj_wywolanie("za_rzeka")
    elif dzialanie == 2:
        print (
            u"\nStwierdzasz, ze nie musisz (przynajmniej na razie) przechodzic\n"
            u"na druga strone, wiec zawracasz."
        )
        dodaj_wywolanie("rozdroze")
    elif dzialanie == 3:
        print (
            u"\nDostrzegasz na drugim brzegu przybity kolek, o ktory\n"
            u"z powodzeniem moglbys zaczepic line rzucajac jej petelka zawiazana\n"
            u"na koncu. Brakuje Ci jedynie czegos, do czego moglbys ja przywiazac.\n"
            u"Lina jest za krotka, aby mozna bylo ja obwiazac wokol drzewa."
        )
        if "Kolek" not in ekwipunek:
            print (
                u"Rezygnujesz wiec pomyslu przeplyniecia przez rwaca rzeke\n"
                u"trzymajac sie liny i wracasz do rozdroza."
            )
            dodaj_wywolanie("rozdroze")
        else:
            print (
                u"\nPrzypominasz sobie nagle o kolku z nory, ktory zachowales.\n"
                u"Wbijasz go w ziemie. Rzucasz lina na drugi brzeg. Trafiles\n"
                u"idealnie w kolek! Drugi koniec zahaczasz o swoj i przeplywasz\n"
                u"przez rzeke trzymajac sie kurczowo liny.\n"
                u"Udaje Ci sie dotrzec na drugi brzeg. Chociaz jestes calkowicie\n"
                u"przemoczony, odczuwasz zadowolenie. Wziales line i zauwazyles,\n"
                u"ze malo brakowalo do jej rozerwania. Nie wrocisz na drugi brzeg.\n"
            )
            dodaj_wywolanie("za_rzeka")

def za_rzeka():
    print (
        u"\nMimo braku mozliwosci powrotu idziesz hardo sciezka. Na jej koncu\n"
        u"znajdujesz niewielka, drewniana chatke.\n"
        u"1. Wejdz do chatki.\n"
        u"2. Zawroc."
    )
    while True:
        dzialanie = wybor(2)
        if dzialanie == 1:
            dodaj_wywolanie("wiedzma")
            return
        elif dzialanie == 2:
            print u"\nNie ma sensu wracac!"

def wiedzma():
    global decyzje
    global ekwipunek
    bilans = 0
    licznik_klamstw = 0
    print (
        u"\nWchodzisz do chatki, a przed Toba pojawia sie stara kobieta o siwych\n"
        u"wlosach."
    )
    # Pytanie pierwsze: jedzenie
    jedzenie = None
    if "Jedzenie" in ekwipunek:
        print (
            u"\n- Nie jadlam nic od tygodni, moglbys mi dac swoje jedzenie?\n"
            u"Byles zaskoczony jej wiedza na temat Twoich jagodek.\n"
            u"1. Daj jej jedzenie.\n"
            u"2. Powiedz, ze nie masz jedzenia."
        )
        dzialanie = wybor(2)
        if dzialanie == 1:
            jedzenie = True
        else:
            jedzenie = False
    if jedzenie != None:
        if jedzenie == True:
            print (
                u"\n- Jestes hojnym czlowiekiem! Zostaw sobie to jedzenie."
            )
            bilans += 1
        else:
            print (
                u"\n- Nie chcesz dzielic sie z bliznim? Niech tak bedzie!"
            )
            bilans -= 1
    #print ("licznik_klamstw =", licznik_klamstw)
    #print ("bilans =", bilans)
    # Pytania moralne
    print (
        u"\nPodrapala sie po glowie i powiedziala:\n"
        u"- Nie powinienes byl wchodzic do zakazanego lasu. Nalezy czytac znaki.\n"
        u"Masz szczescie, ze doszedles tu do mnie. Pomoge Ci, ale najpierw\n"
        u"odpowiedz mi na kilka pytan, od ktorych zalezy, jak sie skonczy\n"
        u"twa podroz. Nie probuj zadnych sztuczek, bo jestem w stanie\n"
        u"Cie zabic jednym machnieciem reki.\n\n"
        u"Zaprezentowala to machajac reka i niszczac wazon stojacy na stole.\n"
    )
    # Pytanie drugie: przejscie przez rzeke
    print (
        u"- Na poczatek chcialabym sie dowiedziec, jak przeszedles przez rzeke?\n"
        u"1. \"Zwalilem drzewo.\"\n"
        u"2. \"Przeplynalem. Nie widac?\""
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
    # Pytanie trzecie: zabojstwo
    print (
        u"- Zalozmy, ze Ci wierze. Kolejne pytanie: czy zabiles kiedys\n"
        u"zywe stworzenie?\n"
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
    # Pytanie czwarte: milosiernosc
    print (
        u"- Czasami nie mamy wyboru, ale gdy go mamy, to czesto nie\n"
        u"wykorzystujemy go dobrze... Nastepne pytanie! Czy pomogles\n"
        u"kiedys jakiemus stworzeniu b e z i n t e r e s o w n i e ?\n"
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
        u"- Nalezy byc milosiernym dla blizniego, nawet najwiekszego wroga!\n"
        u"Ostatnie pytanie: czy widziales gdzies moze pewna przerosnieta,\n"
        u"zielona mrowke? Zgubila mi sie...\n"
        u"1. \"Tak.\"\n"
        u"2. \"Nie.\""
    )
    odpowiedz = wybor(2)
    print (
        u"- To bez znaczenia!\n"
        u"Wiedzma zamyslila sie...\n"
    )
    # Podsumowanie
    if licznik_klamstw == 0:
        print u"- Nie oklamales mnie..."
    else:
        print u"- Cos krecisz..."
    if jedzenie != None:
        if jedzenie:
            print u"- Chciales podarowac mi jedzenie..."
        else:
            print u"- Pozalowales mi jedzenia..."
    if decyzje["rzeka_drzewo"]:
        print u"- Zniszczyles nature..."
    else:
        print u"- Szanujesz nature..."
    if not (decyzje["wilk"] and decyzje["pomoc"]):
        print u"- Zabiles zywe stworzenie..."
    else:
        print u"- Nie dokonales nigdy zabojstwa..."
    if decyzje["nora"] and decyzje["pomoc"]:
        print u"- Pomogles blizniemu..."
    elif decyzje["nora"]:
        print u"- Zignorowales blizniego w potrzebie..."
    bilans -= licznik_klamstw
    #print ("licznik_klamstw =", licznik_klamstw)
    #print ("bilans =", bilans)
    if bilans < 0:
        print (
            u"- Byc moze dzialales zgodnie ze swoim sumieniem, ale to za malo!\n"
            u"Obawiam sie, ze nie moge Cie wypuscic z tego lasu.\n\n"
            u"Wiedzma machnela reka i nagle poczules, jak Twoje cialo dretwieje.\n"
            u"Po co wchodziles do zakazanego lasu?\n"
        )
        dodaj_wywolanie("przegrana")
    else:
        print (
            u"- Dobrze! Niech Ci bedzie, pozwole Ci wrocic, ale musze uzyc magii,\n"
            u"ktora bywa kaprysna. Mnie przekonales, przekonaj teraz nature!\n"
            u"Oto jej zagadka:\n\n"
            u"P i e r w s z e to w wyscigu ostatniemu mowiono kierowcy,\n"
            u"D r u g i e to drugie pol skladnika szkieletu.\n"
            u"1. \"Ostatni Trup?\"\n"
            u"2. \"Samochod?\"\n"
            u"3. \"Wolnosc?\"\n"
            u"4. \"Patrz na droge, bo umrzesz?\"\n"
            u"5. \"Prawo?\""
        )
        odpowiedz = wybor(5)
        if odpowiedz == 3:
            print (
                u"Nagle poczules, jakby cos Cie wyrzucilo w powietrze\n"
                u"i zaczelo Ci sie krecic w glowie, az w koncu straciles\n"
                u"przytomnosc. Obudziles sie pomiedzy wejsciem do\n"
                u"Zakazanego Lasu a swoim domem. To bylo ciekawe\n"
                u"przezycie...\n"
            )
            dodaj_wywolanie("wygrana")
        else:
            print (
                u"Wiedzma posepniala.\n"
                u"- To zla odpowiedz... Twoj szczatki beda spoczywaly w tym\n"
                u"lesie. Przykro mi!\n\n"
                u"Machnela reka."
            )
            dodaj_wywolanie("przegrana")

def szelest():
    global decyzje
    if decyzje["szelest"]:
        print (
            u"\nZmierzasz w strone krzakow, w ktorej spotkales wilka, ale szybko\n"
            u"stwierdzasz, ze nie powinienes tam isc drugi raz."
        )
        dodaj_wywolanie("rozdroze")
    else:
        decyzje["szelest"] = True
        print (
            u"\nPodchodzisz ostroznie do krzakow, z ktorych wydobyl sie tajemniczy szelest.\n"
            u"Upewniajac sie, ze nic Ci nie grozi, przekraczasz je i odkrywasz, ze\n"
            u"w tym miejscu zostal slad po dawnej drodze. Uradowany z powodu odkrycia\n"
            u"i zaciekawiony podazasz nia dalej. Po kilku minutach zaczales sie\n"
            u"zastanawiac, czy aby na pewno jestes jeszcze na drodze. Doszedles\n"
            u"do wniosku, ze nie. Zdezorientowany nie mozesz znalezc drogi powrotnej.\n"
            u"Zgubiles sie.\n"
            u"Jednak nie masz wyboru, nie mozesz tu zostac. Zauwazasz mech rosnacy na\n"
            u"drzewie, ktory wskazuje polnoc. W ktorym kierunku isc?\n"
            u"1. Polnoc. Drzewa wydaja Ci sie troche inne niz pozostale...\n"
            u"2. Wschod. Slychac stamtad dzwieki, jakby jakies zwierze cos jadlo.\n"
            u"3. Poludnie. Wydobywa sie stamtad dziwny zapach.\n"
            u"4. Zachod. Rowniez cos czujesz w nozdrzach..."
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
        u"\nPoznajesz miejsce, w ktorym sie znalazles. Patrzysz na mech\n"
        u"i decydujesz sie pojsc tym razem w inna strone.\n"
        u"1. Polnoc. Drzewa wydaja Ci sie troche inne niz pozostale...\n"
        u"2. Wschod. Slychac stamtad dzwieki, jakby jakies zwierze cos jadlo.\n"
        u"3. Poludnie. Wydobywa sie stamtad dziwny zapach.\n"
        u"4. Zachod. Rowniez cos czujesz w nozdrzach..."
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
            print u"Juz tam byles!"

def szelest_polnoc():
    global decyzje
    decyzje["szelest_polnoc"] = True
    print (
        u"\nPostanowiles ruszyc na polnoc. Idziesz ostroznie deptajac\n"
        u"po galeziach. Nagle slyszysz glosny trzask i ogromny bol w nodze.\n"
        u"Z przerazeniem obserwujesz, jak pulapka zakleszczyla sie\n"
        u"na Twojej nodze. Upadasz i zwijasz sie z bolu. Slyszysz zmierzajace\n"
        u"w Twoim kierunku wilki, ktore zwabil zapach krwi. Przypatruja sie\n"
        u"Tobie, ich kolejnej ofiarze. Juz wiesz, ze to sie zle skonczy.\n"
        u"Jeden z wilkow rzuca sie do Twojego gardla i juz nawet nie probujesz\n"
        u"sie bronic. Po co poszedles do tego zakazengo lasu?\n"
    )
    dodaj_wywolanie("przegrana")

def szelest_wschod():
    global decyzje
    global ekwipunek
    decyzje["szelest_wschod"] = True
    print (
        u"Im bardziej zblizasz sie do zrodla niepokojacych dzwiekow,\n"
        u"tym bardziej Twoj strach sie nasila. Po pewnym czasie dostrzegasz\n"
        u"zwloki sarny, ktorymi zajadal sie wilk. Wstrzymujesz oddech\n"
        u"i cofasz sie, ale niechcacy lamiesz galazke, przez co drapieznik\n"
        u"Cie zauwaza. Zaczynasz uciekac w niewiadomym kierunku.\n"
        u"Wydaje Ci sie, ze trwalo to wiecznosc, ale jakims cudem trafiles\n"
        u"do znajomego rozdroza. Zatrzymujesz sie i ogladasz sie za siebie,\n"
        u"aby sprawdzic, czy wilk biegnie za Toba. Niestety tak!\n"
    )
    if "Bron" not in ekwipunek and "Jedzenie" not in ekwipunek:
        print (
            u"Jestes zbyt wycienczony biegiem, by dalej uciekac. Czekasz, az\n"
            u"drapieznik sie zblizy i liczysz na to, ze uda Ci sie wykorzystac\n"
            u"szanse i sie obronic. Wilk skacze na Ciebie i dopada do gardla.\n"
            u"Mimo wszelkich wysilkow, nie udaje Ci sie go odepchnac.\n"
            u"Po co wszedles do zakazanego lasu?\n"
        )
        dodaj_wywolanie("przegrana")
    elif "Bron" in ekwipunek:
        print (
            u"Jestes zbyt wycienczony biegiem, by dalej uciekac. Czekasz, az\n"
            u"drapieznik sie zblizy i liczysz na to, ze uda Ci sie wykorzystac\n"
            u"szanse i obronic sie.\n"
            u"Przypominasz sobie o nozu, ktory znalazles. Wydobywasz go z kieszeni.\n"
            u"Wilk skacze na Ciebie, a Ty machasz nozem na oslep. Czujesz opor.\n"
            u"Otwierasz oczy i widzisz wykrwawiajace sie zwierze.\n"
            u"Po co wszedles do zakazanego lasu?\n"
            u"Czekasz, az wilk przestanie sie ruszac. Chowasz jego cialo za krzakami."
        )
        decyzje["wilk"] = False
        dodaj_wywolanie("rozdroze")
    elif "Jedzenie" in ekwipunek:
        print (
            u"Nie zastanawiajac sie dlugo, postanawiasz rzucic sie do dalszej\n"
            u"ucieczki. Nie masz pojecia, jaka sciezke wybrales, ale biegniesz.\n"
            u"Nagle widzisz przed soba rzeke i zaczynasz myslec, ze wszystko stracone.\n"
            u"Jednak ogladasz sie za siebie i widzisz, ze wilk juz Cie nie goni.\n"
            u"Uradowany poisz sie woda z rzeki po czym wracasz sciezka."
        )
        decyzje["wilk"] = True
        dodaj_wywolanie("rozdroze")

def szelest_poludnie():
    global decyzje
    global ekwipunek
    decyzje["szelest_poludnie"] = True
    print (
        u"\nNiewiele krokow musiales przejsc, aby dostrzec, skad wydobywa\n"
        u"sie nieprzyjemny zapach. Na ziemi leza zwloki, szkielet czlowieka.\n"
        u"Odruchowo zatykasz nos i cofasz sie, ale po chwili podchodzisz,\n"
        u"aby sprawdzic, czy nie ma tu przypadkiem czegos przydatnego.\n"
        u"Poza dlugim i dosyc ostrym nozem i lina nie znajdujesz nic godnego uwagi.\n"
        u"Bierzesz go ze soba, razem z dluga lina."
    )
    ekwipunek.append("Bron")
    ekwipunek.append("Lina")
    dodaj_wywolanie("szelest_hub")

def szelest_zachod():
    global decyzje
    global ekwipunek
    decyzje["szelest_zachod"] = True
    print (
        u"\nRuszasz w kierunku krzakow na zachodzie. Po kilku sekundach\n"
        u"z niedowierzaniem dostrzegasz rosnace jagody. Nagle przypomnialo\n"
        u"Ci sie, ze jestes glodny, wiec zaczales jesc. Odczules przyplyw\n"
        u"energii i wiary w siebie. Bierzesz troche na droge.\n"
        u"Zgubiles kierunek, ale idziesz dalej."
    )
    ekwipunek.append("Jedzenie")
    dodaj_wywolanie("szelest_hub")

def powrot():
    global decyzje
    if not decyzje["drzewo"]:
        print (
            u"\nOdwracasz sie na piecie i idziesz wydeptana wczesniej przez siebie\n"
            u"sciezka. Nagle, niespodziewanie upada przed Toba drzewo.\n"
            u"Wystraszony cofasz sie i postanawiasz obejsc przeszkode idac\n"
            u"na okolo, ale gdy tylko zblizasz sie do krawedzi sciezki,\n"
            u"zaczynasz slyszec ciezkie dyszenie i warczenie.\n"
            u"Lepiej poszukac innej drogi."
        )
        decyzje["drzewo"] = True
    else:
        print (
            u"\nIdziesz w strone zawalonego drzewa. Juz z oddali widzisz, ze\n"
            u"nic sie nie zmienilo. Probujesz obejsc przeszkode, ale\n"
            u"niebezpieczenstwo czajace sie za sciezka jest zbyt przerazajace.\n"
            u"Zdenerwowany wracasz do rozdroza."
        )

    dodaj_wywolanie("rozdroze")

def dom():
    print (
        u"Wracasz do domu. Nie masz ochoty na zadne przygody."
    )
    dodaj_wywolanie("wygrana")

def wygrana():
    print (
        u"\n\n"
        u"Gratulacje! Wygrales! Chcesz sprobowac jeszcze raz?\n"
        u"1. Tak.\n"
        u"2. Nie."
    )
    jeszcze_raz = wybor(2)

    if jeszcze_raz == 1:
        print u"Doskonale! Moze odkryjesz cos nowego...\n"
        dodaj_wywolanie("start")
    elif jeszcze_raz == 2:
        exit(0)

def przegrana():
    print (
        u"Zginales. Chcesz sprobowac jeszcze raz?\n"
        u"1. Tak.\n"
        u"2. Nie."
    )
    jeszcze_raz = wybor(2)

    if jeszcze_raz == 1:
        print u"Doskonale! Nie poddajesz sie! Moze odkryjesz cos nowego...\n"
        dodaj_wywolanie("start")
    elif jeszcze_raz == 2:
        exit(0)

def reset():
    global ekwipunek
    global decyzje

    # Bron, Lina, Jedzenie, Kolek
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