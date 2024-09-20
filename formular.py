from menu import Menu
from evidence import Evidence


class Formular:
    def __init__(self):
        self.evidence = Evidence()  # Инициализация класса для работы с пользователями
        print("--------------------")
        print("Evidence pojištěných")
        print("--------------------")
        self.spustit()

    def spustit(self):
        pokracovat = "ano"
        while pokracovat.lower() == "ano":
            Menu()  # Вывод меню
            volba = int(input())
            match volba:

                case 1:
                    # Добавление нового pojištěnce
                    while True:
                        jmeno = input("Zadejte jméno pojisteného: ").strip()
                        if not jmeno or not jmeno.isalpha():
                            print("Jméno nesmí být prázdné a musí obsahovat pouze písmena.")
                        else:
                            break

                        # Ввод фамилии с валидацией
                    while True:
                        prijmeni = input("Zadejte přijméní pojisteného: ").strip()
                        if not prijmeni or not prijmeni.isalpha():
                            print("Přijmení nesmí být prázdné a musí obsahovat pouze písmena.")
                        else:
                            break

                        # Ввод возраста с валидацией
                    while True:
                        vek = input("Zadejte vek pojisteného: ").strip()
                        if not vek.isdigit():
                            print("Věk musí být číslo.")
                            continue
                        vek_int = int(vek)
                        if not (0 < vek_int <= 130):
                            print("Věk musí být v rozmezí od 1 do 130.")
                        else:
                            break

                        # Ввод телефона
                    telefon = input("Zadejte telefon pojisteného: ").strip()
                    self.evidence.add_pojisteny(jmeno, prijmeni, vek, telefon)
                    print(f"Pojištěný {jmeno} {prijmeni} úspěšně přidán.")

                case 2:
                    # Вывод всех pojištěnců без использования класса Evidence
                    if self.evidence.seznam:
                        print("\nSeznam všech pojištěných:")
                        for pojisteny in self.evidence.seznam:
                            print(pojisteny)
                    else:
                        print("Žádní pojištěnci nejsou v evidenci.")

                case 3:
                    # Поиск pojištěnce

                    hledane_jmeno = input("Zadejte jméno nebo přijmení pro vyhledání: ").strip()

                    nalezeni = False
                    for pojisteny in self.evidence.seznam:
                        if (pojisteny.jmeno.lower() == hledane_jmeno.lower() or
                                pojisteny.prijmeni.lower() == hledane_jmeno.lower()):
                            print(pojisteny)
                            nalezeni = True
                    if not nalezeni:
                        print("Pojištěný s tímto jménem nebo přijmením nebyl nalezen.")

                case 4:
                    # Завершение работы
                    print("Děkuji za použití aplikace.")
                    break

            if volba != 4:
                pokracovat = input("Přejete si zadat další akci? [ano/ne]: ")
            else:
                break
