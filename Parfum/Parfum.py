import random


class Parfum:
    def termek(rekord, hanyszor, milyentermek,  celcsoport, illatfajta):
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
        file3 = open(celcsoport, "r")
        nev3 = file3.readlines()
        for sor3 in nev3:
            masodik_adat += sor3.splitlines()
        file4 = open(illatfajta, "r")
        nev4 = file4.readlines()
        for sor4 in nev4:
            harmadik_adat += sor4.splitlines()

        # ran = random.choice(nev)
        # for i in sor:
        while rekord <= hanyszor:
            masodik = random.choice(masodik_adat)
            harmadik = random.choice(harmadik_adat)
            print("INSERT INTO " + milyentermek + " VALUES('" + str(rekord) + "', '" + masodik + "', '" + harmadik + "');")
            rekord += 1

        file3.close()
        # file2.close()
        # file3.close()
