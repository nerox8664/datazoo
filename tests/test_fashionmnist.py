import datazoo

if __name__ == '__main__':
	fashionmnist = datazoo.data_provider('fashionmnist', 'data/fashionmnist/', 'test', download=True, columns=['index', 'image'])
	print('len:', len(fashionmnist))
	for i in fashionmnist:
		print(i)
	print(fashionmnist[2])
