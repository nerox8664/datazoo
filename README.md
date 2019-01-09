# Data zoo

This repository provides unified access to the multiple datasets.

## Usage

First of all, you have to import data_provider from datazoo package:

```
from datazoo import data_provider
```

Then, you can use dataset from the list:

```
# Dataset object
fashionmnist = data_provider(
	dataset='fashionmnist',	data_dir='data/fashionmnist/', split='test',
	download=True, columns=['index', 'image', 'class']
)

print('Dataset length:', len(fashionmnist))

# Iterate over samples
for i in fashionmnist:
    print(i) 
```

## Classification

### Single-label datasets

| Dataset | Name in data provider| Number of classes | Number of samples | Source | Auto downloading |
| --- | ---: |---: | ---: | ---: | ---: |  ---: |
| MNIST | `mnist` |10 | 60 000 / 10 000 | torchvision | Yes |
| Fashion MNIST | `fashionmnist`| 10 | 60 000 / 10 000 | torchvision | Yes |
| CIFAR-10 | `cifar10` | 10 | 50 000 / 10 000 | torchvision | Yes |
| CIFAR-100 | `cifar100` | 100 | 50 000 / 10 000 | torchvision | Yes |
| [Indoor Scene Recognition](http://web.mit.edu/torralba/www/indoor.html) | `indoor_scene_recon` | 67 | 15620 | -- | Yes |
| [The Street View House Numbers (SVHN)](http://ufldl.stanford.edu/housenumbers/) | `svhn_cropped` | 10 | 73257 digits for training, 26032 digits for testing, and 531131 additional | -- | Yes |

<!-- ### Multiple labels datasets -->
<!-- 
## Segmentation

| Dataset | Number of classes | Number of samples | Description | Source |
| --- | ---: | ---: | ---: | ---: |
| ADE20k | 10 | 60 000 / 10 000 | General-purpose scene parsing | torchvision | -->