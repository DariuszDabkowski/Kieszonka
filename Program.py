# I added some commentary to the code, but not much, because rest is self explanatory!
import os #library to clear conlose
print("Witaj w programie\n\"Kieszonka\"\ndo zarządzania i planowania wydatków i przychodów\n\nMenu:\n 1) Dodaj wypłatę\n 2) Dodaj inny przychód\n 3) Dodaj czynsz mieszkaniowy\n 4) Dodaj jednorazowy wydatek\n 5) Usuń wpis\n 6) Saldo\n 7) Wyjście z programu")
number = int(input("Podaj numer: "))
data = open('data.txt', 'r', encoding="utf-8").read().split('\n')
value = 0 # value is id number for data.txt entries
for i in data:
        value += 1
while number != 7: #number is option from menu to choose
    if number == 1:
        os.system("cls") #Clearing console
        year = int(input("Podaj rok, w którym będzie wypłata: "))
        os.system("cls")
        month = int(input("Podaj miesiąc, w którym będzie wypłata: "))
        while month < 1 or month > 12: #Checking if month number is valid
            os.system("cls")
            month = int(input("Błędna ilość, podaj jeszcze raz: "))
        os.system("cls")
        amount = int(input("Podaj kwotę wypłaty: "))
        description = "Wypłata"
        data = open('data.txt', "a", encoding="utf-8")
        data.write("\n"+str(value+1)+", "+str(amount)+", "+str(month)+", "+str(year)+", "+str(description)+";")
        data.close()
        os.system("cls")
        print("Witaj w programie\n\"Kieszonka\"\ndo zarządzania i planowania wydatków i przychodów\n\nMenu:\n 1) Dodaj wypłatę\n 2) Dodaj inny przychód\n 3) Dodaj czynsz mieszkaniowy\n 4) Dodaj comiesięczny wydatek(np. opłata za studia, czy abonament telefonu) \n 5) Dodaj jednorazowy wydatek\n 6) Usuń wpis\n 7) Saldo\n 8) Wyjście z programu")
        number = int(input("Podaj numer: "))
    if number == 2:
        os.system("cls")
        description = input("Podaj opis przychodu: ")
        os.system("cls")
        year = int(input("Podaj rok, w którym będzie przychodu: "))
        os.system("cls")
        month = int(input("Podaj miesiąc, w którym będzie przychod: "))
        while month < 1 or month > 12:
            os.system("cls")
            month = int(input("Błędna ilość, podaj jeszcze raz: "))
        os.system("cls")
        amount = int(input("Podaj kwotę przychodu: "))
        data = open('data.txt', "a", encoding="utf-8")
        data.write("\n" + str(value + 1) + ", " + str(amount) + ", " + str(month) + ", " + str(year) + ", " + str(description) + ";")
        data.close()
        os.system("cls")
        print("Witaj w programie\n\"Kieszonka\"\ndo zarządzania i planowania wydatków i przychodów\n\nMenu:\n 1) Dodaj wypłatę\n 2) Dodaj inny przychód\n 3) Dodaj czynsz mieszkaniowy\n 4) Dodaj comiesięczny wydatek(np. opłata za studia, czy abonament telefonu) \n 5) Dodaj jednorazowy wydatek\n 6) Usuń wpis\n 7) Saldo\n 8) Wyjście z programu")
        number = int(input("Podaj numer: "))
    if number == 3:
        os.system("cls")
        year = int(input("Podaj rok, w którym będzie czynsz do zapłaty: "))
        os.system("cls")
        month = int(input("Podaj miesiąc, w którym będzie czynsz do zapłaty: "))
        while month < 1 or month > 12:
            os.system("cls")
            month = int(input("Błędna ilość, podaj jeszcze raz: "))
        os.system("cls")
        amount = int(input("Podaj kwotę czynszu: "))
        description = "Czynsz"
        data = open('data.txt', "a", encoding="utf-8")
        data.write("\n"+str(value+1)+", "+str(-amount)+", "+str(month)+", "+str(year)+", "+str(description)+";")
        data.close()
        os.system("cls")
        print("Witaj w programie\n\"Kieszonka\"\ndo zarządzania i planowania wydatków i przychodów\n\nMenu:\n 1) Dodaj wypłatę\n 2) Dodaj inny przychód\n 3) Dodaj czynsz mieszkaniowy\n 4) Dodaj jednorazowy wydatek\n 5) Usuń wpis\n 6) Saldo\n 7) Wyjście z programu")
        number = int(input("Podaj numer: "))
    if number == 4:
        os.system("cls")
        description = input("Podaj opis wydatku: ")
        os.system("cls")
        year = int(input("Podaj rok, w którym będzie wydatek: "))
        os.system("cls")
        month = int(input("Podaj miesiąc, w którym będzie wydatek: "))
        while month < 1 or month > 12:
            os.system("cls")
            month = int(input("Błędna ilość, podaj jeszcze raz: "))
        os.system("cls")
        amount = int(input("Podaj kwotę wydatku: "))
        os.system("cls")
        data = open('data.txt', "a", encoding="utf-8")
        data.write("\n"+str(value+1)+", "+str(-amount)+", "+str(month)+", "+str(year)+", "+str(description)+";")
        data.close()
        print("Witaj w programie\n\"Kieszonka\"\ndo zarządzania i planowania wydatków i przychodów\n\nMenu:\n 1) Dodaj wypłatę\n 2) Dodaj inny przychód\n 3) Dodaj czynsz mieszkaniowy\n 4) Dodaj jednorazowy wydatek\n 5) Usuń wpis\n 6) Saldo\n 7) Wyjście z programu")
        number = int(input("Podaj numer: "))
    if number == 5:
        os.system("cls")
        deleteid = int(input("Podaj indeks wpisu do usunięcia: ")) - 1
        with open('data.txt', "r", encoding="utf-8") as file:
            data = file.readlines()
        if 0 <= deleteid < len(data):
            data[deleteid] = str(deleteid+1) + ", 0, 0, 0, 0;\n"
        else:
            print("Nieprawidłowy indeks!")
        with open('data.txt', "w", encoding="utf-8") as file:
            file.writelines(data)
        for entry in data:
            print(entry)
        os.system("cls")
        print("Witaj w programie\n\"Kieszonka\"\ndo zarządzania i planowania wydatków i przychodów\n\nMenu:\n 1) Dodaj wypłatę\n 2) Dodaj inny przychód\n 3) Dodaj czynsz mieszkaniowy\n 4) Dodaj jednorazowy wydatek\n 5) Usuń wpis\n 6) Saldo\n 7) Wyjście z programu")
        number = int(input("Podaj numer: "))
    if number == 6:
        os.system("cls")
        data = open('data.txt', 'r', encoding="utf-8").read().split('\n')
        print("Indeks\tKwota\tMiesiąc\tRok\tOpis")
        for data in data:
            print(data)
        print("\nWitaj w programie\n\"Kieszonka\"\ndo zarządzania i planowania wydatków i przychodów\n\nMenu:\n 1) Dodaj wypłatę\n 2) Dodaj inny przychód\n 3) Dodaj czynsz mieszkaniowy\n 4) Dodaj jednorazowy wydatek\n 5) Usuń wpis\n 6) Saldo\n 7) Wyjście z programu")
        number = int(input("Podaj numer: "))
