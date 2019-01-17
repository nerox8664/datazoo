from PIL import Image
from datazoo.common.utils import *
from scipy.io import loadmat
import patoolib
from glob import glob

from os import listdir, rmdir
from shutil import move

class Linnaeus5:
    def __init__(self, data_dir, split, download):
        """
        Linnaeus5 dataset.
        :param data_dir: source/target folder with data
        :param split: 'train', 'test' or 'extra'
        :param download: download dataset and place to `data_dir`
        """
        self.urls = [
            'http://chaladze.com/l5/img/Linnaeus%205%20256X256.rar',
        ]

        self.data_dir = data_dir

        self.data_files = {
            'train': os.path.join(self.data_dir, 'train'),
            'test': os.path.join(self.data_dir, 'test'),
        }
        self.img_dir = self.data_files[split]

        if download:
            self.download()
        
        self.labels = {k:i for i, k in enumerate(os.listdir(self.img_dir))}

        self.images = recursive_glob(self.img_dir)


    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        """
        Get item with index
        :param index: index to return
        :return: dict with all the possible fields
        """
        img = self.images[index]
        target = self.labels[os.path.basename(os.path.dirname(img))]
        
        img = Image.open(img)

        return {
            'index': index,
            'image': img,
            'class': target,
        }

    def _check_exists(self):
        return os.path.exists(self.img_dir)

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
            if not os.path.exists(file_path):
                download_url(url, root=self.data_dir, filename=filename)
            patoolib.extract_archive(file_path, outdir=self.data_dir)

            root = os.path.join(self.data_dir, 'Linnaeus 5 256X256')
            for filename in os.listdir(root):
                move(os.path.join(root, filename), self.data_dir)
            rmdir(root)

        print('Done!')