class Phonebook:

    def __init__(self):
        self.numbers = {}

    def add(self, name, number): 
        self.numbers[name] = number

    def lookup(self, name):
        # Name is in a dictionary numbers
        return self.numbers[name]

    def is_consistent(self):
        return True