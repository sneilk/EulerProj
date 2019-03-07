import os.path
from tempfile import gettempdir

class File:
	def __init__(self, path, data=""):
		self.path = path
		if data:
			self.write(data)

	def __add__(self, file_to_sum):
		return File(os.path.join(gettempdir(), 'third.txt'), self.read() + file_to_sum.read())

	def __str__(self):
		return self.path

	def __iter__(self):
		self.current = 0
		return self

	def __next__(self):
		lines = self.read().split('\n') 
		if self.current >= len(lines):
			raise StopIteration
		self.current += 1
		return lines[self.current - 1]

	def read(self):
		with open(self.path, 'r') as f:
			data = f.read()
		return data

	def write(self, data):
		with open(self.path, 'w') as f:
			f.write(data)


		

obj = File("C:\\python_data\\files and descriptors\\tmp\\file.txt")
obj.write("""4 Углубленный Python 2
4.1 Особые методы классов . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
4.1.1 Магические методы . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
4.1.2 Итераторы . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
4.1.3 Контекстные менеджеры . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4.2 Механизм работы классов . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.2.1 Дескрипторы . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.2.2 Метаклассы . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.3 Отладка и тестирование . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.3.1 Отладка . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.3.2 Тестирование""")
obj2 = File("C:\\python_data\\files and descriptors\\tmp\\file2.txt")
obj2.write("""Оглавление
	""")
obj3 = obj2 + obj
print(obj3)