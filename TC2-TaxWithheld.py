# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("\nTax Withholding Calculator\n")

    salary=float(input("Please enter the full amount of your weekly salary: "))

    dep=float(input("How many dependents do you have?: "))

    proTax = 0.06 * float(salary)

    fedTax = 0.25 * float(salary)

    tWith = proTax + fedTax

    tHome =salary - tWith

    depDed = dep * (0.02 * salary)

    if depDed >= 0:
        tHome = (salary + (dep * (0.02 * salary))) - tWith
        tWith = tWith - depDed

    print("\nProvincial Tax Withheld: ${0:.2f}".format(proTax))

    print("Federal Tax Withheld: ${0:.2f}".format(fedTax))

    print("Dependent Deduction for {0:.0f} dependents: ${1:.2f}".format(dep,depDed))

    print("Total Withheld: ${0:.2f}".format(tWith))

    print("Total Take-Home Pay: ${0:.2f}".format(tHome))
      

    # YOUR CODE ENDS HERE

main()
