from TaxAbstruct import TaxAbstruct
from CommonDeductions import CommonDeductions

class IncomeTax(TaxAbstruct):
    # 所得税算出 https://www.nta.go.jp/publication/pamph/koho/kurashi/html/02_1.htm
    @classmethod
    def calc(cls, total_income):
        # 給与所得額 = 合計所得金額 - 給与所得控除額
        earned_income = total_income - CommonDeductions.earned_income_decustion(total_income)
        # 課税所得額 = 給与所得額 - 所得控除額
        taxable_income = earned_income - cls.__calc_income_deduction(total_income)
        return cls.__calc_tax(taxable_income)

    # 所得控除 https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/shoto320.htm
    @classmethod
    def __calc_income_deduction(cls, total_income):
        deduction = 0.0

        # 基礎控除
        deduction += cls.__calc_basic_deduction(total_income)

        # 社会保険料控除
        deduction += CommonDeductions.social_insurance(total_income)

        # TODO: implement
        # 配偶者控除
        # 配偶者特別控除
        # 扶養控除
        # 障害者控除
        # 寡婦(寡夫)控除
        # 勤労学生控除
        # 雑損控除
        # 医療費控除
        # 小規模企業共済等掛金控除
        # 生命保険料控除
        # 地震保険料控除
        # 寄附金控除

        return deduction        

    @classmethod
    def __calc_tax(cls, taxable_income):
        income_tax = cls.__calc_income_tax(taxable_income)
        return income_tax + IncomeTax.__calc_reconstruction_tax(income_tax)

    # 基礎控除 https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm
    @staticmethod
    def __calc_basic_deduction(total_income, afterR2 = True):
        if afterR2: # 令和2年以降
            if total_income <= 2400:
                return 48.0
            elif total_income <= 2450:
                return 32.0
            elif total_income <= 2500:
                return 16.0
            else:
                return 0.0
        else:
            return 38.0

    # 所得税額 https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm 
    @staticmethod
    def __calc_income_tax(taxable_income):
        if taxable_income <= 195:
            return taxable_income * 0.05
        elif taxable_income <= 330:
            return taxable_income * 0.1 - 9.75
        elif taxable_income <= 695:
            return taxable_income * 0.20 - 42.75
        elif taxable_income <= 900:
            return taxable_income * 0.23  - 63.6
        elif taxable_income <= 1800:
            return taxable_income * 0.33 - 153.6
        elif taxable_income <= 4000:
            return taxable_income * 0.4 - 279.6
        else:
            return taxable_income * 0.45 - 479.6          
    
    # 復興特別所得税額 https://www.nta.go.jp/publication/pamph/koho/kurashi/html/02_1.htm
    @staticmethod
    def __calc_reconstruction_tax(income_tax):
        return income_tax * 0.021