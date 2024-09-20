from pojisteny import Pojisteny


class Evidence:
    def __init__(self):
        self.seznam = []  # Список всех pojištěnců

    def add_pojisteny(self, jmeno, prijmeni, vek, telefon):

        # Если все данные введены корректно, создаем объект pojištěnce и добавляем в список
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.seznam.append(pojisteny)
