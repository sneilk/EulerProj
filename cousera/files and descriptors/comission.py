class Value:

	def __set__(self, obj, row_amount):
		obj.clean_amount = row_amount - row_amount * obj.commission

	def __get__(self, obj, obj_type):
		return int(obj.clean_amount)

class Account:
	amount = Value()

	def __init__(self, commission):
		self.commission = commission
		self.amount = 0

new_account = Account(2)
new_account.amount = 200
print(new_account.amount)
new_account.amount = 110
print(new_account.amount)
new_account1 = Account(0.2)
new_account1.amount = 110
print(new_account1.amount)
print(new_account.amount)
