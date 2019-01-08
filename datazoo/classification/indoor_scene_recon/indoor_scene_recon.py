from __future__ import print_function
from PIL import Image

import sys
import tarfile
from datazoo.common.utils import *

from os import listdir, rmdir
from shutil import move

import pkg_resources

resource_package = __name__
train_resource_path = 'TrainImages.txt'
test_resource_path = 'TestImages.txt'

train_resource_stream = pkg_resources.resource_stream(resource_package, train_resource_path)
test_resource_stream = pkg_resources.resource_stream(resource_package, test_resource_path)


class IndoorSceneRecon:
    def __init__(self, data_dir, split, download):
        self.urls = [
            'http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09.tar',
        ]

        self.train_list = [str(i.decode('ascii')).rstrip() for i in train_resource_stream]
        self.test_list = [str(i.decode('ascii')).rstrip() for i in test_resource_stream]

        self.class_mapping = {
            k: i for i, k in enumerate(sorted(np.unique([i.split('/')[0] for i in self.train_list])))
        }

        self.filename = 'indoorCVPR_09.tar'
        self.data_dir = data_dir

        if download:
            self.download()

        if split == 'train':
            self.data = self.train_list
        else:
            self.data = self.test_list

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            dict: dictionary with all available data
        """

        class_name, _ = self.data[index].split('/')
        img, target = self.data[index], int(self.class_mapping[class_name])

        img = Image.open(os.path.join(self.data_dir, img))

        return {
            'index': index,
            'image': img,
            'class': target,
        }

    def _check_exists(self):
        root = self.data_dir
        for fentry in (self.train_list + self.test_list):
            fpath = os.path.join(root, fentry)
            if not os.path.exists(fpath):
                return False
        return True

    def download(self):
        """Download the dataset data if it doesn't exist."""

        if self._check_exists():
            return

        makedir_exist_ok(self.data_dir)

        print('Downloading...')

        # download files
        for url in self.urls:
            filename = url.rpartition('/')[2]
            file_path = os.path.join(self.data_dir, filename)
            if not os.path.exists(file_path):
                download_url(url, root=self.data_dir, filename=filename)

        print('Processing...')

        # extract file
        with tarfile.open(os.path.join(self.data_dir, self.filename), "r:tar") as tar:
            tar.extractall(path=self.data_dir)

            root = os.path.join(self.data_dir, 'Images/')
            for filename in listdir(root):
                move(os.path.join(root, filename), self.data_dir)
            rmdir(root)

        print('Done!')
