from abc import ABC, abstractmethod

class TaxAbstruct(ABC):
    @classmethod
    @abstractmethod
    def calc(cls, total_income, additional_diduction = 0):
        pass
    
    @classmethod
    @abstractmethod
    def __calc_income_deduction(cls, total_income):
        pass

    @classmethod
    @abstractmethod
    def __calc_tax(cls, taxable_income):
        pass
    