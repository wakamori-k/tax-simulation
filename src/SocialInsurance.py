class SocialInsurance:
    # 社会保険料
    @staticmethod
    def calc(total_income):
        deduction = 0
        # 健康保険, 厚生年金 https://www.kyoukaikenpo.or.jp/~/media/Files/shared/hokenryouritu/r2/ippan/r2030113tokyo.pdf
        deduction += total_income * 0.0987 / 2
        deduction += total_income * 0.183 / 2

        # 雇用保険 https://www.mhlw.go.jp/content/000484772.pdf
        deduction += total_income * 0.003
        
        return deduction