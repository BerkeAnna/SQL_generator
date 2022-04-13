from Telefon import telefon
from TV import TV
from Mosogep import Mosogep
from Grill import Grillsuto
from Horgaszbot import Horgaszbot
from Parfum import Parfum
from Kerekpar import Kerekpar
from Vasarlo import Vasarlo
from Termekek import Termekek
from Termekek import Telotermekek


class main:
    print("Tabla neve: ")
    milyentermek = input()
    if milyentermek == "Termek":
        print("Telo marka / -")
        gyarto = input()
    print("Hany rekord? ")
    hanyszor = int(input())
    print("Hanyadik rekordtol? ")
    rekord = int(input())
    hanyszor2 = hanyszor

    if milyentermek == "Telefon":
        telo = telefon.Telefon.termek(rekord, hanyszor2, milyentermek, "Telefon/telefonkijelzotipus.txt",
                                      "Telefon/telefonkijelzofelbontas.txt",
                                      "Telefon/telefonram.txt", "Telefon/telefonbelsomemoria.txt",
                                      "Telefon/hatlapikamerafelb.txt")


    elif milyentermek == "TV":
        tv = TV.TV.termek(rekord, hanyszor2, milyentermek, "TV/TVkijelzo.txt",
                          "TV/telefonkijelzofelbontas.txt",
                          "TV/szelessegmagassag.txt")

    elif milyentermek == "Mosogep":
        mosogep = Mosogep.Mosogep.termek(rekord, hanyszor2, milyentermek, "Mosogep/Mosogepenergiaosztaly.txt",
                                         "Mosogep/Mosogepkapacitas.txt",
                                         "Mosogep/Mosogepsulyenergiaf.txt", "Mosogep/Mosogepsulyvizf.txt")


    elif milyentermek == "Horgaszbot":
        bot = Horgaszbot.Horgaszbot.termek(rekord, hanyszor2, milyentermek, "Horgaszbot/Horgaszbottipus.txt",
                                           "Horgaszbot/Horgaszbotdobosuly.txt",
                                           "Horgaszbot/Horgaszbotresz.txt", "Horgaszbot/Horgaszbothossz.txt")


    elif milyentermek == "Grillsuto":
        grill = Grillsuto.Grillsuto.termek(rekord, hanyszor2, milyentermek, "Grill/Grilluzemanyag.txt",
                                           "Grill/Grillfelulet.txt",
                                           "Grill/szelmag.txt", "Grill/szelmag.txt")


    elif milyentermek == "Parfum":
        parfum = Parfum.Parfum.termek(rekord, hanyszor2, milyentermek, "Parfum/Parfumcelcsoport.txt",
                                      "Parfum/Parfumillatfajta.txt")


    elif milyentermek == "Kerekpar":
        kerekpar = Kerekpar.Kerekpar.termek(rekord, hanyszor2, milyentermek, "Kerekpar/Kerekpartipus.txt",
                                            "Kerekpar/Kerekparcelcsoport.txt",
                                            "Kerekpar/Kerekparvazanyag.txt", "Kerekpar/Kerekparvazmeret.txt")

    elif milyentermek == "Vasarlo":
        vas = Vasarlo.Vasarlo.termek(rekord, hanyszor2, milyentermek, "Vasarlo/felhasznalonev.txt",
                                     "Vasarlo/Vasarlojelszo.txt",
                                     "Vasarlo/VasarloVezeteknev.txt", "Vasarlo/VasarloKeresztnev.txt",
                                     "Vasarlo/VasarloVaros.txt", "Vasarlo/Vasarloutca.txt", "Vasarlo/Vasarloutcatipus.txt",

                                     "Vasarlo/Szamlaszam.txt", )

    elif milyentermek == "Termek":
        if gyarto == "-":
            Termekek.Termekek.termek(rekord, hanyszor2, milyentermek, "Termekek/nev.txt", "Termekek/nev.txt","Termekek/darab.txt", "Termekek/ar.txt" )
        elif gyarto == "telo":
            Telotermekek.Termekek.termek(rekord, hanyszor2, milyentermek, "Telefon/telefonmarka.txt","Telefon/ram.txt", "Termekek/darab.txt", "Termekek/ar.txt")
        elif gyarto == "tv":
            Telotermekek.Termekek.termek(rekord, hanyszor2, milyentermek, "TV/TVmarka.txt", "Termekek/darab.txt", "Termekek/ar.txt")
        elif gyarto == "mosogep":
            Mosogep.Mosogep.termek(rekord, hanyszor2, milyentermek, "Mosogep/Mosogepmarka.txt","Mosogep/Mosogepnev.txt", "Termekek/darab.txt", "Termekek/ar.txt")
        elif gyarto == "horgaszbot":
            Mosogep.Mosogep.termek(rekord, hanyszor2, milyentermek, "Horgaszbot/Horgaszbotmarka.txt","Horgaszbot/Horgaszbotnev.txt", "Termekek/darab.txt", "Termekek/ar.txt")
        elif gyarto == "kerekpar":
            Mosogep.Mosogep.termek(rekord, hanyszor2, milyentermek, "Kerekpar/Kerekparmarka.txt","Kerekpar/Kerekparnev.txt", "Termekek/darab.txt", "Termekek/ar.txt")
        elif gyarto == "parfum":
            Mosogep.Mosogep.termek(rekord, hanyszor2, milyentermek, "Parfum/Parfummarka.txt","Termekek/nev.txt", "Termekek/darab.txt", "Termekek/ar.txt")
        elif gyarto == "grill":
            Mosogep.Mosogep.termek(rekord, hanyszor2, milyentermek, "Grill/Grillmarka.txt", "Grill/Grillnev.txt",
                                   "Termekek/darab.txt", "Termekek/ar.txt")

    #
    # def termek(hanyszor, milyentermek, marka, kijelzotipus, kijelzofelbontas, ram, belsomem, hatlapkam):
    #     global sor2
    #     s = []
    #     masodik_adat = []
    #     harmadik_adat = []
    #     negyedik_adat = []
    #     otodik_adat = []
    #     hatodik_adat = []
    #     file = open(marka, "r")
    #     nev = file.readlines()
    #     for sor in nev:
    #         sor = sor.splitlines()
    #     # print(sor)
    #     file3 = open(kijelzotipus, "r")
    #     nev3 = file3.readlines()
    #     for sor3 in nev3:
    #         masodik_adat += sor3.splitlines()
    #     file4 = open(kijelzofelbontas, "r")
    #     nev4 = file4.readlines()
    #     for sor4 in nev4:
    #         harmadik_adat += sor4.splitlines()
    #     file5 = open(ram, "r")
    #     nev5 = file5.readlines()
    #     for sor5 in nev5:
    #         negyedik_adat += sor5.splitlines()
    #     file6 = open(belsomem, "r")
    #     nev6 = file6.readlines()
    #     for sor6 in nev6:
    #         otodik_adat += sor6.splitlines()
    #     file7 = open(hatlapkam, "r")
    #     nev7 = file7.readlines()
    #     for sor7 in nev7:
    #         hatodik_adat += sor7.splitlines()
    #     ran = random.choice(nev)
    #     #for i in sor:
    #     if ran == 'Apple\n':
    #             n= 'Apple'
    #             file2 = open("Iphone.txt", "r")
    #             nev2 = file2.readlines()
    #             for sor2 in nev2:
    #                 s += sor2.splitlines()
    #             # print(s)
    #             var = random.choice(s)
    #             masodik = random.choice(masodik_adat)
    #             harmadik = random.choice(harmadik_adat)
    #             harmadik2 = random.choice(harmadik_adat)
    #             negyedik = random.choice(negyedik_adat)
    #             otodik = random.choice(otodik_adat)
    #             hatodik = random.choice(hatodik_adat)
    #             print("INSERT INTO " + milyentermek + " VALUES('" + n + "', '" + var + "', '" + masodik + "' ',"
    #                   + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + otodik + ", " + hatodik + ");")
    #     elif ran == 'Honor\n':
    #                 n='Honor'
    #                 file2 = open("Honor.txt", "r")
    #                 nev2 = file2.readlines()
    #                 for sor2 in nev2:
    #                     s += sor2.splitlines()
    #                 # print(s)
    #                 var = random.choice(s)
    #                 masodik = random.choice(masodik_adat)
    #                 harmadik = random.choice(harmadik_adat)
    #                 harmadik2 = random.choice(harmadik_adat)
    #                 negyedik = random.choice(negyedik_adat)
    #                 otodik = random.choice(otodik_adat)
    #                 hatodik = random.choice(hatodik_adat)
    #                 print("INSERT INTO " + milyentermek + " VALUES('" + n + "', '" + var + "', '" + masodik + "' ',"
    #                       + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + otodik + ", " + hatodik + ");")
    #     elif ran == 'Huawei\n':
    #                 n='Huawei'
    #                 file2 = open("Huawei.txt", "r")
    #                 nev2 = file2.readlines()
    #                 for sor2 in nev2:
    #                     s += sor2.splitlines()
    #                 # print(s)
    #                 var = random.choice(s)
    #                 masodik = random.choice(masodik_adat)
    #                 harmadik = random.choice(harmadik_adat)
    #                 harmadik2 = random.choice(harmadik_adat)
    #                 negyedik = random.choice(negyedik_adat)
    #                 otodik = random.choice(otodik_adat)
    #                 hatodik = random.choice(hatodik_adat)
    #                 print("INSERT INTO " + milyentermek + " VALUES('" + n + "', '" + var + "', '" + masodik + "' ',"
    #                       + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + otodik + ", " + hatodik + ");")
    #     elif ran == 'Sony\n':
    #         n = 'Sony'
    #         file2 = open("Sony.txt", "r")
    #         nev2 = file2.readlines()
    #         for sor2 in nev2:
    #             s += sor2.splitlines()
    #         # print(s)
    #         var = random.choice(s)
    #         masodik = random.choice(masodik_adat)
    #         harmadik = random.choice(harmadik_adat)
    #         harmadik2 = random.choice(harmadik_adat)
    #         negyedik = random.choice(negyedik_adat)
    #         otodik = random.choice(otodik_adat)
    #         hatodik = random.choice(hatodik_adat)
    #         print("INSERT INTO " + milyentermek + " VALUES('" + n + "', '" + var + "', '" + masodik + "' ',"
    #               + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + otodik + ", " + hatodik + ");")
    #     elif ran == 'Xiaomi\n':
    #         n = 'Xiaomi'
    #         file2 = open("Xiaomi.txt", "r")
    #         nev2 = file2.readlines()
    #         for sor2 in nev2:
    #             s += sor2.splitlines()
    #         # print(s)
    #         var = random.choice(s)
    #         masodik = random.choice(masodik_adat)
    #         harmadik = random.choice(harmadik_adat)
    #         harmadik2 = random.choice(harmadik_adat)
    #         negyedik = random.choice(negyedik_adat)
    #         otodik = random.choice(otodik_adat)
    #         hatodik = random.choice(hatodik_adat)
    #         print("INSERT INTO " + milyentermek + " VALUES('" + n + "', '" + var + "', '" + masodik + "' ',"
    #               + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + otodik + ", " + hatodik + ");")
    #     elif ran == 'Samsung\n':
    #         n = 'Samsung'
    #         file2 = open("Samsung.txt", "r")
    #         nev2 = file2.readlines()
    #         for sor2 in nev2:
    #             s += sor2.splitlines()
    #         # print(s)
    #         var = random.choice(s)
    #         masodik = random.choice(masodik_adat)
    #         harmadik = random.choice(harmadik_adat)
    #         harmadik2 = random.choice(harmadik_adat)
    #         negyedik = random.choice(negyedik_adat)
    #         otodik = random.choice(otodik_adat)
    #         hatodik = random.choice(hatodik_adat)
    #         print("INSERT INTO " + milyentermek + " VALUES('" + n + "', '" + var + "', '" + masodik + "' ',"
    #               + harmadik + "x" + harmadik2 + "', " + negyedik + ", " + otodik + ", " + hatodik + ");")
    #     file.close()
    #     #file2.close()
    #     # file3.close()
