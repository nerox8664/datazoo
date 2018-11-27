import datazoo

if __name__ == '__main__':
	mnist = datazoo.data_provider('mnist', 'data/', 'test', download=True, columns=['index', 'index'])
	print('len:', len(mnist))
	for i in mnist:
		print(i)
	print(mnist[2])
