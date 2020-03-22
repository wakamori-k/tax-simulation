class CommonDeductions:
    # 社会保険料
    @staticmethod
    def social_insurance(total_income):
        deduction = 0
        # 健康保険, 厚生年金 https://www.kyoukaikenpo.or.jp/~/media/Files/shared/hokenryouritu/r2/ippan/r2030113tokyo.pdf
        deduction += total_income * 0.0987 / 2
        deduction += total_income * 0.183 / 2

        # 雇用保険 https://www.mhlw.go.jp/content/000484772.pdf
        deduction += total_income * 0.003
        
        return deduction

    # 給与所得控除額 https://www.nta.go.jp/publication/pamph/koho/kurashi/html/02_1.htm
    @staticmethod
    def earned_income_decustion(total_income):
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