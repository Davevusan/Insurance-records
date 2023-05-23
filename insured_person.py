class Insured:
    """
    Class represents insured person.
    """

    #constructor of the insured person
    def __init__(self, name, surname, age, phone_no):
        self._name = name
        self._surname = surname
        self._age = age
        self._phone_no = phone_no


    def __str__(self):
        return f"Jméno: {self._name.capitalize()}, Příjmení: {self._surname.capitalize()}, Věk: {self._age}, Telefonní číslo: {self._phone_no}"
