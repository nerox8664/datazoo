from datazoo import data_provider

if __name__ == '__main__':
    fashionmnist = data_provider('fashionmnist', 'data/fashionmnist/', split='test', download=True, columns=['index', 'image', 'class'])
    print('len:', len(fashionmnist))
    for i in fashionmnist:
        print(i)
