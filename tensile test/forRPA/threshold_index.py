import pandas as pd

def main_index(address):
	csv_data = pd.read_csv(address)
	strain_list = csv_data['strain'].tolist()
	_index = 0

	for i in range(len(strain_list)):
		if strain_list[i] < 0.0035:
			pass
		elif strain_list[i] >= 0.0035:
			_index = i+2
			break
	return _index