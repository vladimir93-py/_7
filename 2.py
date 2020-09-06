from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, pam):
        self.pam = pam

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        print(f'Consumption fabric for sewing a coat - {round(self.pam / 6.5) + 0.5}')
        return round(self.pam / 6.5) + 0.5

class Costume(Clothes):
    @property
    def consumption(self):
        print(f'Consumption fabric for sewing a costume - {round(2 * self.pam + 0.3) / 100}')
        return round(2 * self.pam + 0.3) / 100


coat = Coat(52)
costume = Costume(193)
print(coat + costume)