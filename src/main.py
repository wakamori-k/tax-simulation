import pandas as pd
import matplotlib.pyplot as plt

from IncomeTax import IncomeTax

def main():
    income_taxs = []
    min_income = 100
    max_income = 5000
    for total_income in range(min_income, max_income):
        # 所得税
        income_taxs.append(IncomeTax.calc(total_income))
        # TODO: 社会保険料

        # TODO: 住民税

    plt.plot(range(min_income, max_income), income_taxs)
    # plt.xlim(min_income, max_income)
    # plt.ylim(min_income, max_income)
    plt.xlabel("earned income [ten thousand yen]")
    plt.ylabel("income tax [ten thousand yen]")
    plt.show()    

if __name__=="__main__":
    main()