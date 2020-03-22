# 給与所得控除額 https://www.nta.go.jp/publication/pamph/koho/kurashi/html/02_1.htm
class EarnedIncomeDeduction:
    @staticmethod
    def calc(total_income):
        if total_income <= 162.5:
            return 65.0
        elif total_income <= 180:
            return total_income * 0.4
        elif total_income <= 360:
            return total_income * 0.3 + 18.0
        elif total_income <= 660:
            return total_income * 0.2 + 54.0
        elif total_income <= 1000:
            return total_income * 0.1 + 120.0
        else:
            return 220.0