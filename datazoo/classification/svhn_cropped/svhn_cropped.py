from PIL import Image
from datazoo.common.utils import *
from scipy.io import loadmat


class SVHN_cropped:
    def __init__(self, data_dir, split, download):
        """
        Housenumbers cropped dataset.
        :param data_dir: source/target folder with data
        :param split: 'train', 'test' or 'extra'
        :param download: download dataset and place to `data_dir`
        """
        self.urls = [
            'http://ufldl.stanford.edu/housenumbers/train_32x32.mat',
            'http://ufldl.stanford.edu/housenumbers/test_32x32.mat',
            'http://ufldl.stanford.edu/housenumbers/extra_32x32.mat',
        ]

        self.data_dir = data_dir

        self.data_files = {
            'train': 'train_32x32.mat',
            'test': 'test_32x32.mat',
            'extra': 'extra_32x32.mat',
        }

        self.data_file = os.path.join(data_dir, self.data_files[split])

        if download:
            self.download()
        
        data_mat = loadmat(self.data_file)

        self.data = data_mat['X']
        self.targets = data_mat['y']

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        """
        Get item with index
        :param index: index to return
        :return: dict with all the possible fields
        """
        img, target = self.data[:, :, :, index], int(self.targets[index]) % 10

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(img)

        return {
            'index': index,
            'image': img,
            'class': target,
        }

    def _check_exists(self):
        return os.path.exists(self.data_file)

    def download(self):
        """
        Download the dataset
        :return:
        """

        if self._check_exists():
            return

        makedir_exist_ok(self.data_dir)

        print('Downloading...')

        # download files
        for url in self.urls:
            filename = url.rpartition('/')[2]
            file_path = os.path.join(self.data_dir, filename)
            download_url(url, root=self.data_dir, filename=filename)

        print('Done!')