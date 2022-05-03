l_pracownikow = int(input())


class Pracownik:
    def __init__(self,imie,wynagrodzenie_brutto):
        self.imie = imie
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
        self.skladka = round(self.wynagrodzenie_brutto*0.1371,2)
        self.ubez_zdr = round((self.wynagrodzenie_brutto-self.skladka)*0.09,2)
        self.zaliczka_pod_doch = round(((self.wynagrodzenie_brutto-111.25-self.skladka)*0.18-46.33)-((self.wynagrodzenie_brutto-self.skladka)*0.0775),0)
        self.do_wyplaty = round(self.wynagrodzenie_brutto - self.skladka - self.ubez_zdr - self.zaliczka_pod_doch,2)
        self.koszt_pracodawcy = round(self.wynagrodzenie_brutto*0.2074,2)

    def __repr__(self):
        return f"{self.imie} {self.do_wyplaty:.2f} {self.koszt_pracodawcy:.2f} {self.wynagrodzenie_brutto+self.koszt_pracodawcy:.2f}"
    
    def koncowy_koszt_pracodawcy(self):
        return self.wynagrodzenie_brutto+self.koszt_pracodawcy


dane_uzytkownikow = []
laczny_koszt = 0

for pp in range(l_pracownikow):
    dane_wejscowe = input()
    dane_uzytkownikow.append(dane_wejscowe)

for dd in dane_uzytkownikow:
    imie = dd.split(' ')[0]
    wynagrodzenie = int(dd.split(' ')[1])
    pracownik = Pracownik(imie,wynagrodzenie)
    print(pracownik)
    laczny_koszt+=pracownik.koncowy_koszt_pracodawcy()


print(f"{laczny_koszt:.2f}")


    
