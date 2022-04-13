import random


class Telefon:
    def termek(rekord, hanyszor, milyentermek, kijelzotipus, kijelzofelbontas, ram, belsomem, hatlapkam):
        global sor2
        s = []
        masodik_adat = []
        harmadik_adat = []
        negyedik_adat = []
        otodik_adat = []
        hatodik_adat = []
        # file = open(marka, "r")
        # nev = file.readlines()
        # for sor in nev:
        #     sor = sor.splitlines()
        # # print(sor)
        file3 = open(kijelzotipus, "r")
        nev3 = file3.readlines()
        for sor3 in nev3:
            masodik_adat += sor3.splitlines()
        file4 = open(kijelzofelbontas, "r")
        nev4 = file4.readlines()
        for sor4 in nev4:
            harmadik_adat += sor4.splitlines()
        file5 = open(ram, "r")
        nev5 = file5.readlines()
        for sor5 in nev5:
            negyedik_adat += sor5.splitlines()
        file6 = open(belsomem, "r")
        nev6 = file6.readlines()
        for sor6 in nev6:
            otodik_adat += sor6.splitlines()
        file7 = open(hatlapkam, "r")
        nev7 = file7.readlines()
        for sor7 in nev7:
            hatodik_adat += sor7.splitlines()
        # ran = random.choice(nev)
        while rekord <= hanyszor:
            masodik = random.choice(masodik_adat)
            harmadik = random.choice(harmadik_adat)
            harmadik2 = random.choice(harmadik_adat)
            negyedik = random.choice(negyedik_adat)
            otodik = random.choice(otodik_adat)
            hatodik = random.choice(hatodik_adat)
            print("INSERT INTO " + milyentermek + " VALUES( '"+ str(rekord) +"', '"  + masodik + "', '"
                  + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + otodik + ", " + hatodik + ");")
            rekord += 1

        file3.close()
