import datazoo

if __name__ == '__main__':
	cifar10 = datazoo.data_provider('cifar10', 'data/cifar10/', 'test', download=True, columns=['index', 'image'])
	print('len:', len(cifar10))
	for i in cifar10:
		print(i)
	print(cifar10[2])
