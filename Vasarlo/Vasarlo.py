import random


class Vasarlo:
    def termek(rekord, hanyszor, milyentermek, felhasznalonev, jelszo, nev, knev, szallitasiCim, utca, hszam, szamlaszam):
        global sor2
        s = []
        masodik_adat = []
        harmadik_adat = []
        negyedik_adat = []
        otodik_adat = []
        hatodik_adat = []
        kilencedik_adat=[]
        tizedik_adat=[]
        hszam_adat=[]
        # file = open(marka, "r")
        # nev = file.readlines()
        # for sor in nev:
        #     sor = sor.splitlines()
        # # print(sor)
        file3 = open(felhasznalonev, "r")
        nev3 = file3.readlines()
        for sor3 in nev3:
            masodik_adat += sor3.splitlines()
        file4 = open(jelszo, "r")
        nev4 = file4.readlines()
        for sor4 in nev4:
            harmadik_adat += sor4.splitlines()
        file5 = open(nev, "r")
        nev5 = file5.readlines()
        for sor5 in nev5:
            negyedik_adat += sor5.splitlines()
        file9 = open(knev, "r")
        nev9 = file9.readlines()
        for sor9 in nev9:
            kilencedik_adat += sor9.splitlines()
        file6 = open(szallitasiCim, "r")
        nev6 = file6.readlines()
        for sor6 in nev6:
            otodik_adat += sor6.splitlines()

        file10 = open(utca, "r")
        nev10 = file10.readlines()
        for sor10 in nev10:
             tizedik_adat += sor10.splitlines()
        file66 = open(hszam, "r")
        nev66 = file66.readlines()
        for sor66 in nev66:
            hszam_adat += sor66.splitlines()

        file7 = open(szamlaszam, "r")
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
            kil = random.choice(kilencedik_adat)
            utca = random.choice(tizedik_adat)
            hszam2 = random.choice(hszam_adat)

            honap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            ho = random.choice(honap)
            napok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30]
            nap = random.choice(napok)
            evek = [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975,
                    1976, 1978, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
                    2003, 2004]
            ev = random.choice(evek)

            print("INSERT INTO " + milyentermek + " VALUES( '"+ str(rekord) +"', '"  + masodik + "', '"
                  + harmadik +  "', '" + negyedik + " " + kil + "', '"+ masodik + "@gmail.com', " + "TO_DATE('"+ str(ev) +" " + str(ho)
                  + " " + str(nap) + "', 'yyyy mm dd')"
                  + ", '" + otodik  +", " + utca + " utca " + hszam2 + " .', " + hatodik + ");")
            rekord += 1

        file3.close()
