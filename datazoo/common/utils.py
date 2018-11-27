from __future__ import print_function

import os
import errno
from tqdm import tqdm
import codecs
import gzip
from six.moves import cPickle as pickle
import numpy as np


def save_dict(filename_, di_):
    with open(filename_, 'wb') as f:
        pickle.dump(di_, f)


def load_dict(filename_):
    with open(filename_, 'rb') as f:
        ret_di = pickle.load(f)
    return ret_di


# From torchvision
def parse_int(b):
    return int(codecs.encode(b, 'hex'), 16)


def read_label_file(path):
    with open(path, 'rb') as f:
        data = f.read()
        assert parse_int(data[:4]) == 2049
        length = parse_int(data[4:8])
        parsed = np.frombuffer(data, dtype=np.uint8, offset=8)
        return np.reshape(parsed, length)


def read_image_file(path):
    with open(path, 'rb') as f:
        data = f.read()
        assert parse_int(data[:4]) == 2051
        length = parse_int(data[4:8])
        num_rows = parse_int(data[8:12])
        num_cols = parse_int(data[12:16])
        parsed = np.frombuffer(data, dtype=np.uint8, offset=16)
        return np.reshape(parsed, [length, num_rows, num_cols])


def makedir_exist_ok(dirpath):
    """
    Python2 support for os.makedirs(.., exist_ok=True)
    """
    try:
        os.makedirs(dirpath)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise


def gen_bar_updater(pbar):
    def bar_update(count, block_size, total_size):
        if pbar.total is None and total_size:
            pbar.total = total_size
        progress_bytes = count * block_size
        pbar.update(progress_bytes - pbar.n)

    return bar_update


def download_url(url, root, filename):
    from six.moves import urllib

    root = os.path.expanduser(root)
    fpath = os.path.join(root, filename)

    makedir_exist_ok(root)

    # downloads file
    try:
        print('Downloading ' + url + ' to ' + fpath)
        urllib.request.urlretrieve(
            url, fpath,
            reporthook=gen_bar_updater(tqdm(unit='B', unit_scale=True))
        )
    except OSError:
        if url[:5] == 'https':
            url = url.replace('https:', 'http:')
            print('Failed download. Trying https -> http instead.'
                  ' Downloading ' + url + ' to ' + fpath)
            urllib.request.urlretrieve(
                url, fpath,
                reporthook=gen_bar_updater(tqdm(unit='B', unit_scale=True))
            )


def extract_gzip(gzip_path, remove_finished=False):
        print('Extracting {}'.format(gzip_path))
        with open(gzip_path.replace('.gz', ''), 'wb') as out_f, \
                gzip.GzipFile(gzip_path) as zip_f:
            out_f.write(zip_f.read())
        if remove_finished:
            os.unlink(gzip_path)