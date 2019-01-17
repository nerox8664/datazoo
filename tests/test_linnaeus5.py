from datazoo import data_provider

if __name__ == '__main__':
    linnaeus5 = data_provider('linnaeus5', 'data/linnaeus5/', split='test', download=True, columns=['index', 'image', 'class'])
    print('len:', len(linnaeus5))
    for i in linnaeus5:
        print(i)
