import os
import tempfile
import argparse
import json

def read_val(path, k_val):
	with open(path, 'r') as f:
		data = f.read()
		if data == "":
			data = r'{"0" : "2"}'
		d_data = json.loads(data)
		if k_val in d_data.keys():
			return d_data[k_val]
	return None

def write_val(path, k_val, add_data):
	with open(path, 'r') as f:
		data = f.read()
	if data == "":
		data = {}
	else:
		data = json.loads(data)
	if k_val in data.keys():
		if type(data[k_val]) == list:
			data[k_val].append(add_data)
		else:
			data[k_val] = [data[k_val], add_data]
		return data
	data[k_val] = add_data
	return data

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.exists(storage_path) == False:
	f = open(storage_path, 'tw')
	f.close()

if args.value is None:
	inp_data = read_val(storage_path, args.key)
	if type(inp_data) == list:
		for i in inp_data[:-1]:
			print(i, end=", ")
		print(inp_data[-1])
	else:
		print(inp_data)
else:
	to_write_data = write_val(storage_path, args.key, args.value)
	with open(storage_path, 'w') as f:
		json.dump(to_write_data, f)

