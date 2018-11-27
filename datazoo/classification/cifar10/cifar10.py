from __future__ import print_function
from PIL import Image

import sys
import tarfile
from datazoo.common.utils import *


class CIFAR10:
    def __init__(self, data_dir, split, download):
        self.urls = [
            'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz',
        ]

        self.train_list = [
            ['data_batch_1', 'c99cafc152244af753f735de768cd75f'],
            ['data_batch_2', 'd4bba439e000b95fd0a9bffe97cbabec'],
            ['data_batch_3', '54ebc095f3ab1f0389bbae665268c751'],
            ['data_batch_4', '634d18415352ddfa80567beed471001a'],
            ['data_batch_5', '482c414d41f54cd18b22e5b47cb7c3cb'],
        ]

        self.test_list = [
            ['test_batch', '40351d587109b95175f43aff81a1287e'],
        ]

        self.filename = 'cifar-10-python.tar.gz'
        self.data_dir = data_dir

        if download:
            self.download()

        if split == 'train':
            downloaded_list = self.train_list
        else:
            downloaded_list = self.test_list

        self.data = []
        self.targets = []
        # now load the picked numpy arrays
        for file_name, checksum in downloaded_list:
            file_path = os.path.join(self.data_dir, 'cifar-10-batches-py', file_name)
            with open(file_path, 'rb') as f:
                if sys.version_info[0] == 2:
                    entry = pickle.load(f)
                else:
                    entry = pickle.load(f, encoding='latin1')
                self.data.append(entry['data'])
                if 'labels' in entry:
                    self.targets.extend(entry['labels'])
                else:
                    self.targets.extend(entry['fine_labels'])

        self.data = np.vstack(self.data).reshape(-1, 3, 32, 32)
        self.data = self.data.transpose((0, 2, 3, 1))  # convert to HWC

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        img, target = self.data[index], int(self.targets[index])

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(img)

        return {
            'index': index,
            'image': img,
            'class': target,
        }

    def _check_exists(self):
        root = os.path.join(self.data_dir, 'cifar-10-batches-py')
        for fentry in (self.train_list + self.test_list):
            filename, md5 = fentry[0], fentry[1]
            fpath = os.path.join(root, filename)
            if not os.path.exists(fpath):
                return False
        return True

    def download(self):
        """Download the MNIST data if it doesn't exist in processed_folder already."""

        if self._check_exists():
            return

        makedir_exist_ok(self.data_dir)

        # download files
        for url in self.urls:
            filename = url.rpartition('/')[2]
            file_path = os.path.join(self.data_dir, filename)
            download_url(url, root=self.data_dir, filename=filename)
            extract_gzip(gzip_path=file_path, remove_finished=False)

        # process and save as torch files
        print('Processing...')

         # extract file
        with tarfile.open(os.path.join(self.data_dir, self.filename), "r:gz") as tar:
            tar.extractall(path=self.data_dir)

        print('Done!')