from abc import ABC, abstractmethod

class TaxAbstruct(ABC):
    @classmethod
    @abstractmethod
    def calc(cls, earned_income):
        pass
    
    @classmethod
    @abstractmethod
    def __calc_income_deduction(cls, earned_income):
        pass

    @classmethod
    @abstractmethod
    def __calc_tax(cls, taxable_income):
        pass
    