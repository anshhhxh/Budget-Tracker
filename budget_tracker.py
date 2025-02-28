class budget:
    def __init__(self):
        self.income={}
        self.expenses={}
    def add_income(self,category,amount):
        if category in self.income:
            self.income[category]+=amount
        else:
            self.income[category]=amount
    def add_expenses(self,category,amount):
        if category in self.expenses:
            self.expenses[category]+=amount
        else:
            self.expenses[category]=amount
    def total_income(self):
        return sum(self.income.values())
    def total_expenses(self):
        return sum(self.expenses.values())
    def summary(self):
        print("Income Summary   :")
        for category,amount in self.income.items():
            print(f"{category}  :   {amount}")
        print("Total Income     :",self.total_income())
        print("Expenses Summary   :")
        for category,amount in self.expenses.items():
            print(f"{category}  :   {amount}")
        print("Total Expenses     :",self.total_expenses())
        print("Net Total    :",self.total_income()-self.total_expenses())

my_budget=budget()
my_budget.add_income('FreeLancing',2500)
my_budget.add_income('Job',3000)
my_budget.add_expenses("Food",2000)
my_budget.add_income("Side Income",2800)
my_budget.add_expenses("Rent",5000)
my_budget.summary()