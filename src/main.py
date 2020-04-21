import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from IncomeTax import IncomeTax
from ResidentTax import ResidentTax
from CommonDeductions import CommonDeductions

def main():
    total_incomes = list(range(300, 900))
    additional_payment = 90 # 年金の追納額

    # 所得税
    income_taxs = np.array(list(map(IncomeTax.calc, total_incomes)))
    income_taxs_add_payment = np.array(list(map(IncomeTax.calc, total_incomes, [additional_payment for _ in range(len(total_incomes))])))

    # 住民税
    resident_taxs = np.array(list(map(ResidentTax.calc, total_incomes)))
    resident_taxs_add_payment = np.array(list(map(ResidentTax.calc, total_incomes, [additional_payment for _ in range(len(total_incomes))])))

    # 社会保険料
    social_insurances = np.array(list(map(CommonDeductions.social_insurance, total_incomes)))

    total_tax = income_taxs + resident_taxs + social_insurances
    total_tax_add_payment = income_taxs_add_payment + resident_taxs_add_payment + social_insurances

    # 通常時と、学生納付特例制度で猶予されていた年金を追納したときの税金の差額
    plt.plot(total_incomes, total_tax-total_tax_add_payment, color="red", label = "total tax")
    plt.plot(total_incomes, income_taxs-income_taxs_add_payment, label="income tax")
    plt.plot(total_incomes, resident_taxs-resident_taxs_add_payment, label="resident tax")
    plt.xlabel("total income [ten thousand yen]")
    plt.ylabel("tax deduction [ten thousand yen]")
    plt.legend()
    # plt.show()
    plt.savefig("tax_diff_when_additional_payment.png")
    plt.close()

    plt.plot(total_incomes, income_taxs, "--", label="Income tax")
    plt.plot(total_incomes, resident_taxs, "--", label="Resident tax")
    plt.plot(total_incomes, social_insurances, "--", label="Social insurance")
    plt.plot(total_incomes, total_tax, label="Total")
    # plt.xlim(0, max(total_incomes))
    # plt.ylim(0, max(total_incomes))
    plt.xlabel("total income [ten thousand yen]")
    plt.ylabel("tax [ten thousand yen]")
    plt.legend()
    # plt.show()
    plt.savefig("tax.png")
    plt.close()

    total_incomes = np.array(total_incomes)    
    income_taxs_rate = income_taxs / total_incomes
    resident_taxs_rate = resident_taxs / total_incomes
    social_insurances_rate = social_insurances / total_incomes
    total_tax_rate = total_tax / total_incomes

    plt.plot(total_incomes, income_taxs_rate, "--", label="Income tax")
    plt.plot(total_incomes, resident_taxs_rate, "--", label="Resident tax")
    plt.plot(total_incomes, social_insurances_rate, "--", label="Social insurance")
    plt.plot(total_incomes, total_tax_rate, label="Total")
    # plt.xlim(0, max(total_incomes))
    # plt.ylim(0, max(total_incomes))
    plt.xlabel("total income [ten thousand yen]")
    plt.ylabel("tax rate")
    plt.legend()
    # plt.show()
    plt.savefig("tax_rate.png")
    plt.close()    

    plt.plot(total_incomes, total_incomes - total_tax, label="After tax income")
    # plt.xlim(0, max(total_incomes))
    # plt.ylim(0, max(total_incomes))
    plt.xlabel("total income [ten thousand yen]")
    plt.ylabel("income [ten thousand yen]")
    plt.legend()
    # plt.show()
    plt.savefig("after_tax_income.png")
    plt.close()    
if __name__=="__main__":
    main()