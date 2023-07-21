"Program that calculate of quantity taxes that each type of person should be pay to State, I used the programming oriented-object paradigm."
"By: Douglas Holanda"

import locale
import sys


class Person:

    def __init__(self, name, income):
        self._name = name
        self._income = income

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

        @property
        def income(self):
            return self._income

        @income.setter
        def name(self, income):
            self._income = income




class Individual(Person):
    def __init__(self, name, income, healthExpenditures):
        super().__init__(name, income)

        self._healthExpenditures = healthExpenditures

    basicTax = 0.0
    def calculateTaxes(self):

        if self._income > 20000.00:
            basicTax = self._income*0.15
        else:
            basicTax = self._income*0.25

        basicTax -= self._healthExpenditures*0.25

        if basicTax < 0.0:
            basicTax = 0.0
        return basicTax

class Company(Person):
    def __init__(self, name, income, numberEmployeers):
        super().__init__(name, income)

        self._numberEmployeers = numberEmployeers

    tax = 0.0
    def calculateTaxes(self):

        if self._numberEmployeers > 10:
            tax = self._income*0.14
        else:
            tax = self._income*0.15
        return tax


def main():
    locale.setlocale(locale.LC_ALL, 'UK')

    individuals = []
    companies = []
    sumTotalIndi = 0.0
    sumTotalComp = 0.0
    sumTotalTaxes = 0.0

    number = int(input("Enter number of people:"))

    i = 0

    while i < number:
        type = input("Individual or company? (i/c):")

        name = input("Name:")

        income = float(input("Income: "))

        if type == "i":
            health = float(input("Health expenditures: "))

            individual = Individual(name, income, health)

            individuals.append(individual)

            print("Processing...\n")



        elif type == "c":
            employeers = int(input("Number of employeers: "))

            company = Company(name, income, employeers)

            companies.append(company)

            print("Processing...\n")


        else:
            print("Non-existent option! Program closed.\n")

            sys.exit(0)

        i += 1

    print("\nGenerating list...\n")

    print("\nPeople of type individual:\n")

    for individual in individuals:

        print(f"Name of people: {individual._name}\nTotal taxes : $ {individual.calculateTaxes():.2f}\n")

        sumTotalIndi += individual.calculateTaxes()

    print("Generating list...\n")

    print("People of type company:\n")

    for company in companies:

        print(f"Name of people: {company._name}\nTotal taxes : $ {company.calculateTaxes():.2f}\n")

        sumTotalComp += company.calculateTaxes()



    print("\nTaxes paid:\n")

    sumTotalTaxes = sumTotalIndi + sumTotalComp

    print(f"Total taxes: $ {sumTotalTaxes:.2f}.")

if __name__:
    main()



