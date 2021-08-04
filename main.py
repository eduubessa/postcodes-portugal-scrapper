import os

from App.Helpers.Scrapper import Scrapper
from App.Models.County import County


def menu():
    print(" ########################################################   ")
    print("|                                                         |")
    print("|  BEM-VINDO AO SCRAPPER DOS CÓDIGOS POSTAIS PORTUGUESES  |")
    print("|                                                         |")
    print(" ########################################################   ")
    print("|                                                         |")
    print("|  Escolha uma opção:                                     |")
    print("|                                                         |")
    print("|  D - Buscar todos distritos                             |")
    print("|  C - Buscar todos concelhos                             |")
    print("|  F - Buscar todos freguesias                            |")
    print("-----------------------------------------------------------")
    option = input()

    if option == "D" or option == "d":
        print("|  A SCRAPPER OS DISTRITOS PORTUGUESES ...  |")
        Scrapper.fetch_districts()
        menu()
    elif option == "C" or option == "c":
        print("|  A SCRAPPER OS CONCELHOS PORTUGUESES ...  |")
        Scrapper.fetch_counties()
        menu()
    elif option == "F" or option == "f":
        print("|  A SCRAPPER OS FREGUESIAS PORTUGUESES ...  |")
        Scrapper.fetch_parishes()
    else:
        print("ERROR OPTION")
        menu()


menu()
