# S8
if __name__ == "__main__": # Local Run
    import Expense
else: # Module Run, When going production - delete if/else
    from . import Expense

# S1
class BudgeList():
	#pass
	
	# S2	
	def __init__(self, budget):
		self.budget = budget
		self.sum_expenses = 0
		self.expenses = []
		self.sum_overages = 0
		self.overages = []

	# S3
	def append(self, item):
		# pass

		# S4 
		if self.sum_expenses + item < self.budget:
			self.expenses.append(item)
			self.sum_expenses += item

		#S5
		else:
			self.overages.append(item)
			self.sum_overages += item

	# S6
	def __len__(self):
		return len(self.expenses) + len(self.overages)

# S7
def main():
	myBudgeList = BudgeList(budget = 1200)

	# S9
	expenses = Expense.Expenses()
	expenses.read_expenses('data/spending_data.csv')

	# S10
	for expense in expenses.list:
		myBudgeList.append(expense.amount)

	# S11
	print('The count of all expenses: ' + str(len(myBudgeList)))

# S12
if __name__ == "__main__":
	main()

