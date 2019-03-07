import os.path
import csv

class BaseCar:
	def __init__(self, car_type, brand, photo_file_name, carrying, *args, **kwargs):
		self.brand = brand
		self.car_type = car_type
		self.photo_file_name = photo_file_name
		self.carrying = float(carrying)

	def get_photo_file_ext(self):
		return(os.path.splitext(self.photo_file_name)[-1])

class Car(BaseCar):
	def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, 
					carrying, *args, **kwargs):
		super().__init__(car_type, brand, photo_file_name, carrying)
		self.passenger_seats_count = int(passenger_seats_count)

class Truck(BaseCar):
	def __init__(self, car_type, brand, photo_file_name, 
					carrying, body_whl, *args, **kwargs):
		super().__init__(car_type, brand, photo_file_name, carrying)
		if body_whl:
			buff = body_whl.split('x')
			self.body_height = float(buff[2])
			self.body_length = float(buff[0])
			self.body_width  = float(buff[1])
		else: 
			self.body_height, self.body_length, self.body_width = 0.0, 0.0, 0.0

	def get_body_volume(self):
		return self.body_width * self.body_length * self.body_height

class SpecMachine(BaseCar):
	def __init__(self, car_type, brand, photo_file_name, 
					carrying, extra, *args, **kwargs):
		super().__init__(car_type, brand, photo_file_name, carrying)
		self.extra = extra

def get_car_list(csv_filename):
	car_list = []
	if os.path.exists(csv_filename):
		with open(csv_filename, 'r') as f:
			data = csv.DictReader(f, delimiter=';')
			for data_dict in data:
				try:
					if data_dict['car_type'] == 'car':
						car_list.append(Car(**data_dict))
					elif data_dict['car_type'] == 'truck':
						car_list.append(Truck(**data_dict))
					elif data_dict['car_type'] == 'spec_machine':
						car_list.append(SpecMachine(**data_dict))
				except:
					continue
	return car_list
