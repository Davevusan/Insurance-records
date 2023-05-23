from insured_person import Insured
from insurance import Insurance
import os

def get_int_input(promt): #int input function
    while True:
        try:
            value = int(input(promt))
            return value
        except ValueError:
            print("Zadejte prosím číselnou hodnotu.")

insurance = Insurance()

while True:
    os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal

    #starting screen
    print("-------------------------------------\n"
          "EVIDENCE POJIŠTĚNCŮ\n"
          "-------------------------------------\n")

    print("Vyberte si akci:\n"
          "1 - Přidat nového pojištěnce\n"
          "2 - Vypsat všechny pojištěnce\n"
          "3 - Vyhledat pojištěnce\n"
          "4 - Konec")


    option = get_int_input("\nVyberte číslo ze seznamu: ")


    match (option):

        case 1: #Creating new insured person

            print("Vytvoření nového pojištěnce:\n")

            name = str(input("Zadejte jméno: "))
            surname = str(input("Zadejte příjmení: "))
            age = get_int_input("Zadejte věk: ")
            phone_no = get_int_input("Zadejte telefonní číslo: ")

            insurance.add_insured(Insured(name, surname, age, phone_no))
            print("Data byla uložena.")
            input("\nPokračujte libovolnou klávesou...")

        case 2: #List all the insured persons

            print("Výpis pojištěnců:\n")
            insurance.print_insured_list()
            input("\nPokračujte libovolnou klávesou...")

        case 3: #Search for specific insured person

            print("Vyhledávání pojištěnce:\n")
            name = str(input("Zadejte jméno: "))
            surname = str(input("Zadejte příjmení: "))

            person = insurance.find_insured(name, surname)

            if person is not None:
                print(person)
            else:
                print("Pojištěnec nebyl nalezen.")

            input("\nPokračujte libovolnou klávesou...")

        case 4: #Quit
            print("Ukončuji evidenci pojištěnců")
            exit()
