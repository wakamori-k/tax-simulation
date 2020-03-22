import pandas as pd
import matplotlib.pyplot as plt

# 給与所得控除額 https://www.nta.go.jp/publication/pamph/koho/kurashi/html/02_1.htm
def calcEarnedIncomeDeduction(earnedIncome):
    if earnedIncome <= 162.5:
        return 65
    elif earnedIncome <= 180:
        return earnedIncome * 0.4
    elif earnedIncome <= 360:
        return earnedIncome * 0.3 + 18
    elif earnedIncome <= 660:
        return earnedIncome * 0.2 + 54
    elif earnedIncome <= 1000:
        return earnedIncome * 0.1 + 120
    else:
        return 220

# 基礎控除 https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm
def calcBasicDeduction(earnedIncome, afterR2 = True):
    if afterR2: # 令和2年以降
        if earnedIncome <= 2400:
            return 48
        elif earnedIncome <= 2450:
            return 32
        elif earnedIncome <= 2500:
            return 16
        else:
            return 0
    else:
        return 38

# 医療費控除
def calcMedicalExpenseDeduction():
    # TODO: implement
    return 0

# 社会保険料控除
def calcSocialInsurance(earnedIncome):
    deduction = 0
    # 健康保険 https://www.kyoukaikenpo.or.jp/~/media/Files/shared/hokenryouritu/r2/ippan/r2030113tokyo.pdf
    deduction += earnedIncome * 0.0987 / 2
    # 厚生年金
    deduction += earnedIncome * 0.183 / 2
    # 雇用保険
    deduction += earnedIncome * 0.003
    return deduction

# その他の所得控除 Ref. https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/shoto320.htm
def calcOtherIncomeDeduction(earnedIncome, afterR2 = True):
    deduction = 0

    # 基礎控除
    deduction += calcBasicDeduction(earnedIncome, afterR2)

    # 社会保険料控除
    deduction += calcSocialInsurance(earnedIncome)

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

# 所得税額 https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm 
def calcIncomeTax(taxableIncome):
    if taxableIncome <= 195:
        return taxableIncome * 0.05
    elif taxableIncome <= 330:
        return taxableIncome * 0.1 - 9.75
    elif taxableIncome <= 695:
        return taxableIncome * 0.20 - 42.75
    elif taxableIncome <= 900:
        return taxableIncome * 0.23  - 63.6
    elif taxableIncome <= 1800:
        return taxableIncome * 0.33 - 153.6
    elif taxableIncome <= 4000:
        return taxableIncome * 0.4 - 279.6
    else:
        return taxableIncome * 0.45 - 479.6

# 復興特別所得税額 https://www.nta.go.jp/publication/pamph/koho/kurashi/html/02_1.htm
def calcReconstructionTax(incomeTax):
    return incomeTax * 0.021

def main():
    incomeTaxs = []
    socialInsurances = []
    afterTaxIncomes = []
    minIncome = 100
    maxIncome = 5000
    for income in range(minIncome, maxIncome):
        # 課税対象所得算出
        taxableIncome = income - calcEarnedIncomeDeduction(income) - calcOtherIncomeDeduction(income)
        incomeTax = calcIncomeTax(taxableIncome) + calcReconstructionTax(taxableIncome)
        incomeTaxs.append(incomeTax)

        socialInsurance = calcSocialInsurance(income)
        socialInsurances.append(socialInsurances)

        afterTaxIncomes.append(income - incomeTax - socialInsurance)

    plt.plot(range(minIncome, maxIncome), afterTaxIncomes)
    plt.xlim(minIncome, maxIncome)
    plt.ylim(minIncome, maxIncome)
    plt.xlabel("earned income [ten thousand yen]")
    plt.ylabel("after-tax income [ten thousand yen]")
    plt.show()    

if __name__=="__main__":
    main()