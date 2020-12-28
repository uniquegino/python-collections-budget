import os
import collections
import matplotlib.pyplot as plt

# S1
if __name__ == "__main__": # Local Run
    import Expense
else: # Module Run, When going production - delete if/else
    from . import Expense

expenses = Expense.Expenses()

# S2
# fname = os.path.abspath('..')+'\data\spending_data.csv'
expenses.read_expenses('data/spending_data.csv')

# S3
spending_categories = []
for expense in expenses.list:
	spending_categories.append(expense.category)

# S4
spending_counter = collections.Counter(spending_categories)
# print(spending_counter)

# S5
top5 = spending_counter.most_common(5)

# S6
categories, count = zip(*top5)

# S7
fig, ax = plt.subplots()

# S8
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

# S9
plt.show()