# Budget-Tracker
# Budget Tracker 💰📊  

A **simple budget tracker** built in Python to help manage income and expenses efficiently. This program allows users to categorize their earnings and expenditures, providing a clear summary of total income, total expenses, and net balance.  

## 🔹 **Features**  
✅ Add income & expenses by category  
✅ Calculate total income & expenses  
✅ Display a summary with net balance  
✅ Easy-to-use and lightweight  

## 🔹 **How It Works**  
1. Add income using `add_income(category, amount)`.  
2. Add expenses using `add_expenses(category, amount)`.  
3. View a detailed financial summary with `summary()`.  

## 🔹 **Example Usage**  
```python
my_budget = Budget()
my_budget.add_income("Freelancing", 2500)
my_budget.add_income("Job", 3000)
my_budget.add_expenses("Food", 2000)
my_budget.add_expenses("Rent", 5000)
my_budget.summary()
```

## 🔹 **Output**  
```
Income Summary:
Freelancing : 2500
Job : 3000
Total Income : 5500

Expenses Summary:
Food : 2000
Rent : 5000
Total Expenses : 7000

Net Total : -1500
```

## 🔹 **Future Enhancements**  
🚀 Add a graphical user interface (GUI)  
🚀 Implement data persistence with a database or CSV  
🚀 Introduce visual analytics for spending insights  

🔗 **Contributions & feedback are welcome!**  

#Python #BudgetTracker #Finance #Coding #OOP
