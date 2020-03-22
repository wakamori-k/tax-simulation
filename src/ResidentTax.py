from TaxAbstruct import TaxAbstruct
from CommonDeductions import CommonDeductions

class ResidentTax(TaxAbstruct):
    # 住民税算出
    @classmethod
    def calc(cls, total_income):
        # 給与所得額 = 合計所得金額 - 給与所得控除額
        earned_income = total_income - CommonDeductions.earned_income_decustion(total_income)
        # 課税所得額 = 給与所得額 - 所得控除額
        taxable_income = earned_income - cls.__calc_income_deduction(total_income)

        return cls.__calc_tax(taxable_income)

    # 所得控除 https://www.tax.metro.tokyo.lg.jp/kazei/kojin_ju.html#gaiyo_08
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
        return taxable_income * 0.1 + 0.5

    # 基礎控除　https://www.e-zeirisi.com/kisokoujo-h30kaisei-12177.html
    @staticmethod
    def __calc_basic_deduction(total_income, afterR2 = True):
        if afterR2: # 令和2年以降
            if total_income <= 2400:
                return 43.0
            elif total_income <= 2450:
                return 29.0
            elif total_income <= 2500:
                return 15.0
            else:
                return 0.0
        else:
            return 33.0