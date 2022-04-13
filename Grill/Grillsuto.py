import random


class Grillsuto:
    def termek(rekord, hanyszor, milyentermek, uzemanyagtipus, grillezofelulet, szelesseg, magassag):
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
        file3 = open(uzemanyagtipus, "r")
        nev3 = file3.readlines()
        for sor3 in nev3:
            masodik_adat += sor3.splitlines()
        file4 = open(grillezofelulet, "r")
        nev4 = file4.readlines()
        for sor4 in nev4:
            harmadik_adat += sor4.splitlines()
        file5 = open(szelesseg, "r")
        nev5 = file5.readlines()
        for sor5 in nev5:
            negyedik_adat += sor5.splitlines()
        file6 = open(magassag, "r")
        nev6 = file6.readlines()
        for sor6 in nev6:
            otodik_adat += sor6.splitlines()
        # ran = random.choice(nev)
        # for i in sor:
        while rekord <= hanyszor:
            masodik = random.choice(masodik_adat)
            harmadik = random.choice(harmadik_adat)
            negyedik = random.choice(negyedik_adat)
            otodik = random.choice(otodik_adat)
            # ran = random.choice(nev)
            print("INSERT INTO " + milyentermek + " VALUES('" + str(
                rekord) + "', '" + masodik + "', '" + harmadik + "', " + negyedik + ", " + otodik + ");")
            rekord += 1

        file3.close()
        # file2.close()
        # file3.close()
