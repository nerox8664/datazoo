import datazoo

if __name__ == '__main__':
	mnist = datazoo.data_provider('mnist', 'data/mnist/', 'test', download=True, columns=['index', 'image'])
	print('len:', len(mnist))
	for i in mnist:
		print(i)
	print(mnist[2])
