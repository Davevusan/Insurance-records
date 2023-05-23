class Insurance:
    """
    Class represents insurance list.
    """

    #constructor of a list of the insured people
    def __init__(self):
        self._insurance_list = []

    #method to add an insured person to the list
    def add_insured(self, person):
        self._insurance_list.append(person)

    #method to search for insured person based on name and surname
    def find_insured(self, name, surname):
        for person in self._insurance_list:
            if person._name == name and person._surname == surname:
                return person

        return None

    #method to print out the list of insured persons
    def print_insured_list(self):
        for person in self._insurance_list:
            print(person)

insurance = Insurance()