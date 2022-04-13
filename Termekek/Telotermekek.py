import random


class Termekek:
    def termek(rekord, hanyszor, milyentermek, gyarto, ram, darab, ar):
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
        file4 = open(gyarto, "r")
        nev4 = file4.readlines()
        for sor4 in nev4:
            harmadik_adat += sor4.splitlines()
        file5 = open(darab, "r")
        nev5 = file5.readlines()
        for sor5 in nev5:
            negyedik_adat += sor5.splitlines()
        file6 = open(ar, "r")
        nev6 = file6.readlines()
        for sor6 in nev6:
            otodik_adat += sor6.splitlines()

        file7 = open(ar, "r")
        nev7 = file7.readlines()
        for sor7 in nev7:
            hatodik_adat += sor7.splitlines()
        # ran = random.choice(nev)
        # for i in sor:
        ran = random.choice(harmadik_adat)
        #for i in sor:
        while rekord <= hanyszor:
            harmadik = random.choice(harmadik_adat)
            negyedik = random.choice(negyedik_adat)
            otodik = random.choice(otodik_adat)
            hatodik = random.choice(hatodik_adat)
            print("INSERT INTO " + milyentermek + " VALUES(" + str(rekord)  + "', '"
                  + harmadik + "', " + hatodik+ ", "+ negyedik + ", " + otodik + ");")
            rekord += 1
        file4.close()
        if ran == 'Apple\n':
            n = 'Apple'
            file2 = open("Iphone.txt", "r")
            nev2 = file2.readlines()
            for sor2 in nev2:
                s += sor2.splitlines()
            # print(s)
            masodik = random.choice(s)
            #masodik = random.choice(masodik_adat)
            harmadik = random.choice(harmadik_adat)
            negyedik = random.choice(negyedik_adat)
            otodik = random.choice(otodik_adat)
            print("INSERT INTO " + milyentermek + " VALUES('" + str(rekord) + "', '" + harmadik + "', '"
                  + masodik + "', " + negyedik + ", " + otodik + ");")
        elif ran == 'Honor\n':
                n = 'Honor'
                file2 = open("Honor.txt", "r")
                nev2 = file2.readlines()
                for sor2 in nev2:
                    s += sor2.splitlines()
                # print(s)
                masodik = random.choice(s)
                # masodik = random.choice(masodik_adat)
                harmadik = random.choice(harmadik_adat)
                negyedik = random.choice(negyedik_adat)
                otodik = random.choice(otodik_adat)
                print("INSERT INTO " + milyentermek + " VALUES(" + str(rekord) + "', '" + masodik + "', '"
                      + harmadik + "', " + negyedik + ", " + otodik + ");")
        elif ran == 'Huawei\n':
                n = 'Huawei'
                file2 = open("Huawei.txt", "r")
                nev2 = file2.readlines()
                for sor2 in nev2:
                    s += sor2.splitlines()
                # print(s)
                masodik = random.choice(s)
                # masodik = random.choice(masodik_adat)
                harmadik = random.choice(harmadik_adat)
                negyedik = random.choice(negyedik_adat)
                otodik = random.choice(otodik_adat)
                print("INSERT INTO " + milyentermek + " VALUES(" + str(rekord) + "', '" + masodik + "', '"
                      + harmadik + "', " + negyedik + ", " + otodik + ");")
        elif ran == 'Sony\n':
                n = 'Sony'
                file2 = open("Sony.txt", "r")
                nev2 = file2.readlines()
                for sor2 in nev2:
                    s += sor2.splitlines()
                # print(s)
                masodik = random.choice(s)
                # masodik = random.choice(masodik_adat)
                harmadik = random.choice(harmadik_adat)
                negyedik = random.choice(negyedik_adat)
                otodik = random.choice(otodik_adat)
                print("INSERT INTO " + milyentermek + " VALUES(" + str(rekord) + "', '" + masodik + "', '"
                      + harmadik + "', " + negyedik + ", " + otodik + ");")
        elif ran == 'Xiaomi\n':
                n = 'Xiaomi'
                file2 = open("Xiaomi.txt", "r")
                nev2 = file2.readlines()
                for sor2 in nev2:
                    s += sor2.splitlines()
                # print(s)
                masodik = random.choice(s)
                # masodik = random.choice(masodik_adat)
                harmadik = random.choice(harmadik_adat)
                negyedik = random.choice(negyedik_adat)
                otodik = random.choice(otodik_adat)
                print("INSERT INTO " + milyentermek + " VALUES(" + str(rekord) + "', '" + masodik + "', '"
                      + harmadik + "', " + negyedik + ", " + otodik + ");")
        elif ran == 'Samsung\n':
                n = 'Samsung'
                file2 = open("Samsung.txt", "r")
                nev2 = file2.readlines()
                for sor2 in nev2:
                    s += sor2.splitlines()
                # print(s)
                masodik = random.choice(s)
                # masodik = random.choice(masodik_adat)
                harmadik = random.choice(harmadik_adat)
                negyedik = random.choice(negyedik_adat)
                otodik = random.choice(otodik_adat)
                print("INSERT INTO " + milyentermek + " VALUES(" + str(rekord) + "', '" + masodik + "', '"
                      + harmadik + "', " + negyedik + ", " + otodik + ");")

        # file2.close()
        # file3.close()
