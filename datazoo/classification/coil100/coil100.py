from __future__ import print_function
from PIL import Image

import sys
import tarfile
from datazoo.common.utils import *
from glob import glob


class COIL100:
    def __init__(self, data_dir, split, download):
        """
        Create a COIL-100 dataset instance.
        :param data_dir: source/target folder with data
        :param split: 'all'
        :param download: download dataset and place to `data_dir`
        """

        self.urls = [
            'http://www.cs.columbia.edu/CAVE/databases/SLAM_coil-20_coil-100/coil-100/coil-100.zip',
        ]

        self.filename = 'coil-100.zip'
        self.data_dir = data_dir

        self.img_dir = os.path.join(self.data_dir, 'coil-100')

        if download:
            self.download()

        self.samples = glob(os.path.join(self.img_dir, '*.png'))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (image, target) where target is index of the target class.
        """

        img_path = self.samples[index]
        target = int(os.path.basename(img_path).split('__')[0][3:]) - 1
        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.open(img_path)

        return {
            'index': index,
            'image': img,
            'class': target,
        }

    def _check_exists(self):
        print(self.img_dir)
        return os.path.exists(self.img_dir)

    def download(self):
        """Download the COIL100 data if it doesn't exist in processed_folder already."""

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
            
            import zipfile
            zip_ref = zipfile.ZipFile(file_path, 'r')
            zip_ref.extractall(self.data_dir)
            zip_ref.close()

        print('Done!')
