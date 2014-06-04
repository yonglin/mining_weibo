import pickle

def keep_data(address,raw_data):
	'''using pickle to store the raw data'''

	filename = address
	data = raw_data
	f = open(filename, 'wb')
	pickle.dump(data, f) # dump the object to a file
	f.close()

def get_data(address):
	'''using pickle to get the raw data'''

	f = open(address, 'rb')
	data = pickle.load(f) # load the object from the file
	f.close()
	return data
	