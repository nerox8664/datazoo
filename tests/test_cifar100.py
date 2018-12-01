import datazoo

if __name__ == '__main__':
	cifar100 = datazoo.data_provider('cifar100', 'data/cifar100/', 'test', download=True, columns=['index', 'image'])
	print('len:', len(cifar100))
	for i in cifar100:
		print(i)
	print(cifar100[2])
