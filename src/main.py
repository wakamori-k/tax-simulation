import pandas as pd
import matplotlib.pyplot as plt

from IncomeTax import IncomeTax

# 給与所得控除額 https://www.nta.go.jp/publication/pamph/koho/kurashi/html/02_1.htm
def calcEarnedIncome(earnedIncome):
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

def main():
    income_taxs = []
    min_income = 100
    max_income = 5000
    for total_income in range(min_income, max_income):
        # 課税対象所得算出
        earned_income = total_income - calcEarnedIncome(total_income)
        income_taxs.append(IncomeTax.calc(earned_income))

    plt.plot(range(min_income, max_income), income_taxs)
    # plt.xlim(min_income, max_income)
    # plt.ylim(min_income, max_income)
    plt.xlabel("earned income [ten thousand yen]")
    plt.ylabel("income tax [ten thousand yen]")
    plt.show()    

if __name__=="__main__":
    main()