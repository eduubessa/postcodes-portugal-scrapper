from App.Helpers.Scrapper import Scrapper

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
        print("|  TERMINOU ! ...  |")
        menu()
    elif option == "C" or option == "c":
        print("|  A SCRAPPER OS DISTRITOS PORTUGUESES ...  |")
        Scrapper.fetch_counties()
        print("|  TERMINOU ! ...  |")
    elif option == "F" or option == "f":
        print("|  A SCRAPPER OS FREGUESIAS PORTUGUESES ...  |")
        Scrapper.fetch_parishes()
        print("|  TERMINOU ! ...  |")

menu()