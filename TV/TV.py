import random


class TV:
    def termek(rekord, hanyszor, milyentermek, kijelzotipus, kijelzofelbontas, szelessegmagassag):
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
        # print(sor)
        file3 = open(kijelzotipus, "r")
        nev3 = file3.readlines()
        for sor3 in nev3:
            masodik_adat += sor3.splitlines()
        file4 = open(kijelzofelbontas, "r")
        nev4 = file4.readlines()
        for sor4 in nev4:
            harmadik_adat += sor4.splitlines()
        file5 = open(szelessegmagassag, "r")
        nev5 = file5.readlines()
        for sor5 in nev5:
            negyedik_adat += sor5.splitlines()
        # ran = random.choice(nev)
        # for i in sor:
        while rekord <= hanyszor:
            masodik = random.choice(masodik_adat)
            harmadik = random.choice(harmadik_adat)
            harmadik2 = random.choice(harmadik_adat)
            negyedik = random.choice(negyedik_adat)
            negyedik2 = random.choice(negyedik_adat)
            print("INSERT INTO " + milyentermek + " VALUES('" + str(rekord) + "', '" + masodik + "', '"
                  + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + negyedik2 + ");")
            rekord+=1
        file3.close()
        # file2.close()
        # file3.close()
