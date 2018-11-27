from .classification import *


class DatasetWrapper:
    """
    Dataset wrapper class
    """
    def __init__(self, dataset, columns):
        """
        Construct the object that is able to extract only specified fields.
        :param dataset: a dataset class
        :param columns: columns to extract
        """
        self.dataset = dataset
        self.columns = columns

    def __len__(self):
        return len(self.dataset)
    
    def  __getitem__(self, idx):
        result = []
        original_data = self.dataset[idx]
        
        if self.columns:
            for i in self.columns:
                result.append(original_data[i])
        else:
            result = original_data.values()

        return tuple(result)


def data_provider(dataset, data_dir, split, download=False, columns=None):
    """
    Dataset creation function
    :param dataset: dataset name
    :param data_dir: data directory
    :param split: 'test' or 'train' mostly
    :param download: should we download the dataset if it's possible
    :param columns: columns to extract
    :return: wrapped dataset
    """
    mapping = {
        'mnist': MNIST,
        'fashionmnist': FashionMNIST,
        'cifar10': CIFAR10,
        'cifar100': CIFAR100,
    }

    return DatasetWrapper(mapping[dataset.lower()](data_dir, split, download), columns)