protokol_okw = {
    "start": [
        { "sub": "entries", "field": "data", "template": "templ_proto" }
    ],
    "entries": [
        { "field": "sin", "num": "xin","type": "longnum", "pri": 0, "ro": 1, "text": "Xin" },
        { "heading": "Dane ogĂłlne", "copy": "submitOuter" },
        { "field": "rola", "num": "D1", "pri": 1, "type": "rola", "text": "Funkcja zgĹaszajÄcego" },
        { "field": "imie", "num": "D2", "pri": 1, "type": "text", "text": "ImiÄ" },
        { "field": "nazwisko", "num": "D3", "pri": 1, "type": "text", "text": "Nazwisko" },

        { "field": "obserwacja_przyg_lokalu", "num": "D5", "pri": 1, "type": "bool+czas+text", "text": "Obserwacja przygotowania lokalu" },
        { "field": "obserwacja_glosowania", "num": "D6", "pri": 1, "type": "bool+czas+text", "text": "Obserwacja gĹosowania" },
        { "field": "obserwacja_liczenia", "num": "D7", "pri": 1, "type": "bool+czas+text", "text": "Obserwacja liczenia gĹosĂłw" },
        { "heading": "Dane o komisji (szare) wypeĹnione automatycznie, bez edycji", "copy": "submitOuter" },
        
        { "field": "woj", "num": "D8", "pri": 1, "ro": 1, "type": "text", "text": "WojewĂłdztwo" },
        { "field": "gmina", "num": "D9", "pri": 1, "ro": 1, "type": "text", "text": "Gmina" },
        { "field": "num_obw", "num": "D10", "pri": 11, "ro": 1, "text": "Nr obwodowej komisji wyborczej <br> (aby zmieniÄ - pĂłjdĹş na gĂłrÄ strony)" },
        { "field": "adres", "num": "D11", "pri": 1, "ro": 1, "type": "text", "text": "Adres komisji" },
        { "field": "siedziba_opis", "num": "D12", "pri": 1, "ro": 1, "type": "text", "text": "Miejsce - opis szczegĂłĹowy" },
        { "field": "komisja_czlonkow", "num": "D13", "pri": 1, "text": "Liczba czĹonkĂłw komisji" },
        { "field": "komisja_osob_upr", "num": "D14", "pri": 1, "text": "Liczba osĂłb uprawnionych do gĹosowania w komisji" },
        { "heading": "Przygotowanie", "copy": "submitOuter" },
        { "field": "P1", "num": "P1", "pri": 1, "type": "bool+text", "text": "Czy komisja jest prawidĹowo oznaczona â na zewnÄtrz i wewnÄtrz lokalu wyborczego?", info: "JeĹźeli nie to dlaczego?" },
        { "field": "P2", "num": "P2", "pri": 1, "type": "bool+text", "text": "Czy po opieczÄtowaniu karty byĹy przechowywane w taki sposĂłb, aby nie miaĹa do nich dostÄpu Ĺźadna osoba nieuprawniona?", info: "JeĹźeli nie to dlaczego?" },
        { "field": "P3", "num": "P3", "pri": 1, "type": "bool+text", "text": "Czy w lokalu wyborczym znajdujÄ siÄ wymagane obwieszczenia i informacje o sposobie gĹosowania?", info: "JeĹźeli nie to dlaczego?" },
        { "field": "P4", "num": "P4", "pri": 1, "type": "bool+text", "text": "Czy w lokalu wyborczym znajdujÄ siÄ miejsca zapewniajÄce tajnoĹÄ gĹosowania?", info: "JeĹźeli nie to dlaczego?" },
        { "field": "P5", "num": "P5", "pri": 1, "type": "bool+text", "text": "Czy w lokalu wyborczym lub na terenie, na ktĂłrym siÄ on znajduje znaleziono jakiekolwiek materiaĹy agitacyjne?", info: "JeĹźeli tak, to jakie i co z nimi zrobiono?" },
        { "field": "P6", "num": "P6", "pri": 1, "type": "bool+text", "text": "Czy komisja w jakimkolwiek momencie utrudniaĹa Ci obserwacjÄ procedury przygotowania lokalu wyborczego do gĹosowania?", info: "JeĹźeli tak, opisz na czym polegaĹy utrudnienia:" },
        { "field": "P7", "num": "P7", "pri": 1, "type": "bool+text", "text": "Czy zgĹaszaĹeĹ komisji uwagi do sposobu jej pracy?", info: "JeĹli tak, to jakie uwagi i jaka byĹa reakcja czĹonkĂłw Komisji?" },
        { "field": "P8", "num": "P8", "pri": 1, "type": "ocena", "text": "OgĂłlna ocena pracy komisji podczas przygotowania" },
        { "field": "P9", "num": "P9", "pri": 1, "type": "textarea", "text": "Dodatkowe komentarze (dot. przygotowania)", info: "Dodatkowe komentarze:" },
        { "heading": "GĹosowanie", "copy": "submitOuter" },
        { "field": "G1", "num": "G1", "pri": 1, "type": "bool+text", "text": "Czy w lokalu wyborczym lub terenie, na ktĂłrym siÄ on znajduje, zdarzyĹ siÄ przypadek agitacji wyborczej?", info: "JeĹĹi tak, to ile takich przypadkĂłw zauwaĹźyĹaĹ/eĹ? ProszÄ opisaÄ te przypadki." },
        { "field": "G2", "num": "G2", "pri": 1, "type": "bool+text", "text": "Czy zdarzyĹo siÄ, Ĺźe czĹonkowie komisji nie sprawdzili komuĹ dokumentu toĹźsamoĹci przed wydaniem kart do gĹosowania?", info: "JeĹli tak, podaj liczbÄ takich przypadkĂłw." },
        { "field": "G3", "num": "G3", "pri": 1, "type": "bool+text", "text": "Czy czĹonkowie komisji caĹy czas korzystali z osĹony na dane osobowe?", info: "JeĹli nie, podaj jak czÄsto z niej nie korzystali (sporadycznie, nagminnie, przez caĹy czas):" },
        { "field": "G4", "num": "G4", "pri": 1, "type": "bool+text", "text": "Czy urna byĹa caĹy czas obserwowana?" },
        { "field": "G5", "num": "G5", "pri": 1, "type": "bool+text", "text": "Czy byĹa osoba peĹniÄca rolÄ 'straĹźnika urny'?" },
        { "field": "G6", "num": "G6", "pri": 1, "type": "bool+text", "text": "Czy byĹa przestrzegana tajnoĹÄ gĹosowania?", info: "JeĹli nie, w jakich sytuacjach (np. tzw. gĹosowanie rodzinne, na widoku, inne) i czy nagminnie czy raczej sporadycznie:" },
        { "field": "G7", "num": "G7", "pri": 1, "type": "czestosc", "text": "Czy komisja interweniowaĹa w przypadkach nieprzestrzegania lub naruszania tajnoĹci gĹosowania?" },
        { "field": "G8", "num": "G8", "pri": 1, "type": "bool+text", "text": "Czy straĹźnik urny lub komisja zawsze reagowaĹa w sytuacji, gdy wyborca wrzucaĹ do urny karty w sposĂłb ujawniajÄcy na kogo oddaĹ gĹos?", info: "JeĹli reagowaĹa, to w jaki sposĂłb:" },
        { "field": "G9", "num": "G9", "pri": 1, "type": "bool+text", "text": "Czy wystÄpiĹy jakiekolwiek problemy zwiÄzane ze zbyt maĹÄ liczbÄ miejsc zapewniajÄcych tajnoĹÄ gĹosowania?", info: "JeĹli tak, opisz jakie:" },
        { "field": "G10", "num": "G10", "pri": 1, "type": "bool+text", "text": "Czy zdarzyĹo siÄ, Ĺźe ktoĹ usiĹowaĹ wynieĹÄ karty do gĹosowania z lokalu wyborczego?", info: "JeĹli tak, podaj liczbÄ takich przypadkĂłw i opisz jak zareagowaĹa Komisja:" },
        { "field": "G11", "num": "G11", "pri": 1, "type": "bool+text", "text": "Czy komisja w dowolnym momencie utrudniaĹa Ci obserwacjÄ procesu gĹosowania?" },
        { "field": "G12", "num": "G12", "pri": 1, "type": "bool+text", "text": "Czy zgĹaszaĹeĹ komisji uwagi do sposobu jej pracy?" },
        { "field": "G13", "num": "G13", "pri": 1, "type": "textarea", "text": "JeĹźeli byĹy takie przypadki, to jak reagowaĹa komisja w sytuacji przybycia nazbyt duĹźej iloĹci gĹosujÄcych?", info: "Opisz pracÄ Komisji w godzinach najwiÄkszego obciÄĹźenia (jednoczesne przybycie nazbyt duĹźej iloĹci gĹosujÄcych):" },
        { "field": "G14", "num": "G14", "pri": 1, "type": "ocena", "text": "OgĂłlna ocena pracy komisji podczas gĹosowania" },
        { "field": "G15", "num": "G15", "pri": 1, "type": "textarea", "text": "Dodatkowe komentarze (dot. gĹosowania)", info: "Dodatkowe komentarze:" },
        { "heading": "Liczenie gĹosĂłw", "copy": "submitOuter" },
        { "field": "L1", "num": "L1", "pri": 1, "type": "bool+text", "text": "Czy urna byĹa zaplombowana w momencie, gdy komisja przystÄpiĹa do jej otwierania?" },
        { "field": "L2", "num": "L2", "pri": 1, "type": "bool+text", "text": "Czy wszyscy czĹonkowie komisji byli obecni w trakcie liczenia?", info: "JeĹźeli nie, opisz kto byĹ nieobecny:" },
        { "field": "L3", "num": "L3", "pri": 1, "type": "bool+text", "text": "Czy komisja przeglÄdaĹa, segregowaĹa i liczyĹa karty i gĹosy dziaĹajÄc wspĂłlnie, nie dzielÄc siÄ na grupy?", info: "Opisz sposĂłb pracy komisji:" },
        { "field": "L4", "num": "L4", "pri": 1, "type": "bool+text", "text": "Czy w urnie znajdowaĹy siÄ materiaĹy inne niĹź opieczÄtowane karty do gĹosowania?", info: "JeĹźeli tak, to co to byĹo?" },
        { "field": "L5", "num": "L5", "pri": 1, "type": "bool+text", "text": "Czy wystÄpiĹy jakiekolwiek problemy z interpretacjÄ waĹźnoĹci gĹosĂłw?", info: "Opisz, na czym polegaĹy problemy:" },
        { "field": "L6", "num": "L6", "pri": 1, "type": "niebylo3t", "text": "Czy w przypadku sporĂłw dotyczÄcych waĹźnoĹci gĹosu komisja podejmowaĹa decyzjÄ wiÄkszoĹciÄ gĹosĂłw?", info: "JeĹźeli nie, to opisz jak decydowaĹa Komisja:" },
        { "field": "L7", "num": "L7", "pri": 1, "type": "bool+text", "text": "Czy wystÄpiĹy jakiekolwiek problemy lub nieprawidĹowoĹci przy wypeĹnianiu protokoĹu?", info: "JeĹźeli tak, opisz je:" },
        { "field": "L8", "num": "L8", "pri": 1, "type": "bool+text", "text": "Czy mÄĹźowie zaufania lub czĹonkowie komisji wnieĹli uwagi do protokoĹu komisji?", info: "JeĹźeli tak, opisz jakie:" },
        { "field": "L9", "num": "L9", "pri": 1, "type": "bezuwag3t", "text": "Czy komisja ustosunkowaĹa siÄ do tych uwag?", info: "JeĹźeli tak, to w jaki sposĂłb:" },
        { "field": "L10", "num": "L10", "pri": 1, "type": "niewiem3t", "text": "Czy wystÄpiĹy jakiekolwiek problemy z wprowadzeniem danych do informatycznego systemu WOW", info: "JeĹźeli tak, to jakie?" },
        { "field": "L11", "num": "L11", "pri": 1, "type": "bool+text", "text": "Czy zdarzyĹ siÄ jakikolwiek przypadek odmowy wydania kopii protokoĹu mÄĹźowi zaufania lub obserwatorowi, jeĹli o niÄ poprosiĹ?" },
        { "field": "L12", "num": "L12", "pri": 1, "type": "bool+text", "text": "Czy komisja wywiesiĹa w miejscu Ĺatwo dostÄpnym dla wyborcĂłw kopie protokoĹĂłw gĹosowania w obwodzie?" },
        { "field": "L13", "num": "L13", "pri": 1, "type": "bool+text", "text": "Czy komisja w jakimkolwiek momencie utrudniaĹa Ci obserwacjÄ procesu liczenia gĹosĂłw?", info: "JeĹli tak, jakie uwagi i jaka byĹa reakcja czĹonkĂłw Komisji?" },
        { "field": "L14", "num": "L14", "pri": 1, "type": "bool+text", "text": "Czy zgĹaszaĹeĹ komisji uwagi do sposobu jej pracy?", info: "JeĹli tak, opisz na czym polegaĹy utrudnienia:" },
        { "field": "L15", "num": "L15", "pri": 1, "type": "text", "text": "O ktĂłrej godzinie komisja zakoĹczyĹa pracÄ?" },
        { "field": "L16", "num": "L16", "pri": 1, "type": "ocena", "text": "OgĂłlna ocena pracy komisji podczas liczenia gĹosĂłw" },
        { "field": "L17", "num": "L17", "pri": 1, "type": "textarea", "text": "Dodatkowe komentarze (liczenie gĹosĂłw)", info: "Dodatkowe komentarze:" },
        { "heading": "Klauzula dot. ochrony danych osobowych", "copy": "submitOuter" },
        { "field": "rodo", "num": "R0", "pri": 1, "ro": 1, "type": "info", "text": "Informacja o przetwarzaniu danych osobowych (RODO)", info: `Zgodnie z art. 13 ust. 1 i ust. 2 ogĂłlnego rozporzÄdzenia o ochronie danych osobowych z dnia 27 kwietnia 2016 r. informujemy, iĹź: 
  1. Administratorem Pani/Pana danych osobowych jest Komitet Obrony Demokracji z siedzibÄ w Warszawie 01-144; GĂłrczewska 39 
  2. Inspektorem ochrony danych w Komitecie Obrony Demokracji jest Pani Beata Somerschaf,
   e-mail: Beata.Somerschaf@ruchkod.pl 
  3. Pani/Pana dane osobowe przetwarzane za pomocÄ tego formularza bÄdÄ uĹźyte w projekcie Obywatelska Kontrola WyborĂłw podczas WyborĂłw Parlamentarnych 2019 r oraz informacji o dziaĹaniach Stowarzyszenia Komitet Obrony Demokracji) na podstawie art. 6 ust 1 pkt a ROZPORZÄDZENIE PARLAMENTU EUROPEJSKIEGO I RADY (UE) 2016/679 
  4. Pani/Pana dane osobowe nie bÄdÄ przekazywane do paĹstwa trzeciego/organizacji miÄdzynarodowej 
  5. Pani/Pana dane osobowe bÄdÄ przechowywane przez okres 5 lat 
  6. Posiada Pani/Pan prawo dostÄpu do treĹci swoich danych oraz prawo ich sprostowania, usuniÄcia, ograniczenia przetwarzania, prawo do przenoszenia danych, prawo wniesienia sprzeciwu, prawo do cofniÄcia zgody w dowolnym momencie bez wpĹywu na zgodnoĹÄ z prawem przetwarzania, ktĂłrego dokonano na podstawie zgody przed jej cofniÄciem 
  7. Ma Pan/Pani prawo wniesienia skargi do GIODO gdy uzna Pani/Pan, iĹź przetwarzanie danych osobowych Pani/Pana dotyczÄcych narusza przepisy ogĂłlnego rozporzÄdzenia o ochronie danych osobowych z dnia 27 kwietnia 2016 r. 
  8. Podanie przez Pana/PaniÄ danych osobowych jest warunkiem umownym. Jest Pan/Pani zobowiÄzana do ich podania a konsekwencjÄ niepodania danych osobowych bÄdzie brak moĹźliwoĹci udziaĹu w projekcie.` }
    ]
}

def_ankieta = {
    numer: 1,
    data: {
        rola: { n: 3, t: " " },
        imie: "",
        nazwisko: "",
        czas_obserwacji_start: "08:00",
        czas_obserwacji_end: "08:00",
        obserwacja_przyg_lokalu: false,
        obserwacja_glosowania: false,
        obserwacja_liczenia: false,
        woj: "",
        gmina: "",
        num_obw: "",
        adres: "",
        siedziba_opis: "",
        komisja_czlonkow: "",
        komisja_osob_upr: 0,
        rodo: " ",
        P1: { b: false, t: "" },
        P2: { b: false, t: "" },
        P3: { b: false, t: "" },
        P4: { b: false, t: "" },
        P5: { b: false, t: "" },
        P6: { b: false, t: "" },
        P7: { b: false, t: "" },
        P8: { n: 0, t: "" },
        P9: "",
        G1: { b: false, t: "" },
        G2: { b: false, t: "" },
        G3: { b: false, t: "" },
        G4: { b: false, t: "" },
        G5: { b: false, t: "" },
        G6: { b: false, t: "" },
        G7: { n: 0, t: "" },
        G8: { b: false, t: "" },
        G9: { b: false, t: "" },
        G10: { b: false, t: "" },
        G11: { b: false, t: "" },
        G12: { b: false, t: "" },
        G13: "",
        G14: { n: 0, t: "" },
        G15: "",
        L1: { b: false, t: "" },
        L2: { b: false, t: "" },
        L3: { b: false, t: "" },
        L4: { b: false, t: "" },
        L5: { b: false, t: "" },
        L6: { v: "", t: "" },
        L7: { b: false, t: "" },
        L8: { b: false, t: "" },
        L9: { v: "", t: "" },
        L10: { v: "", t: "" },
        L11: { b: false, t: "" },
        L12: { b: false, t: "" },
        L13: { b: false, t: "" },
        L14: { b: false, t: "" },
        L15: "",
        L16: { n: 0, t: "" },
        L17: ""
    }
}

entries_data_okw = {
    "1:020101:2": {
        numer: 1,
        data: {
            imie: "Anna",
            nazwisko: "Belska",
            czas_obserwacji_start: "20:00",
            czas_obserwacji_end: "21:00",
            obserwacja_przyg_lokalu: "tak",
            obserwacja_glosowania: "tak",
            obserwacja_liczenia: "tak",
            gmina: "Boles",
            num_obw: "2",
            siedziba: "Szk",
            siedziba_opis: "Sala 22",
            komisja_czlonkow: "7",
            komisja_osob_upr: 800,
            P1: "",
            P2: "",
            P3: "",
            P4: "",
            P5: "",
            P6: "",
            P7: "",
            P8: "",
            P9: "",
            G1: "",
            G2: "",
            G3: "",
            G4: "",
            G5: "",
            G6: "",
            G7: "",
            G8: "",
            G9: "",
            G10: "",
            G11: "",
            G12: "",
            G13: "",
            G14: "",
            G15: "",
            L1: "",
            L2: "",
            L3: "",
            L4: "",
            L5: "",
            L6: "",
            L7: "",
            L8: "",
            L9: "",
            L10: "",
            L11: "",
            L12: "",
            L13: "",
            L14: "",
            L15: ""
        }
    }
};