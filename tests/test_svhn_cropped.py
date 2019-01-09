from datazoo import data_provider

if __name__ == '__main__':
    svhn_cropped = data_provider('svhn_cropped', 'data/svhn_cropped/', split='test', download=True, columns=['index', 'image', 'class'])
    print('len:', len(svhn_cropped))
    for i in svhn_cropped:
        if i[2] == 0:
            i[1].show()
            break
        print(i)
