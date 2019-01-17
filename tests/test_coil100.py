import datazoo

if __name__ == '__main__':
	coil100 = datazoo.data_provider('coil100', 'data/coil100/', 'test', download=True, columns=['index', 'image', 'class'])
	print('len:', len(coil100))
	for i in coil100:
		print(i)
	print(coil100[2])
