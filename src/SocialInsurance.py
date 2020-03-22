class SocialInsurance:
    # 社会保険料
    @staticmethod
    def calc(earnedIncome):
        deduction = 0
        # 健康保険 https://www.kyoukaikenpo.or.jp/~/media/Files/shared/hokenryouritu/r2/ippan/r2030113tokyo.pdf
        deduction += earnedIncome * 0.0987 / 2
        # 厚生年金
        deduction += earnedIncome * 0.183 / 2
        # 雇用保険
        deduction += earnedIncome * 0.003
        return deduction