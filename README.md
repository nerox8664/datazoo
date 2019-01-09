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
fashionmnist = data_provider('fashionmnist', 'data/fashionmnist/', split='test', download=True, columns=['index', 'image', 'class'])

print('Dataset length:', len(fashionmnist))

# Iterate over samples
for i in fashionmnist:
    print(i) 
```

## Classification

### Single-label datasets

| Dataset | Number of classes | Number of samples | Description | Source | Auto downloading |
| --- | ---: | ---: | ---: | ---: |  ---: |
| MNIST | 10 | 60 000 / 10 000 | Hand-written digits | torchvision | Yes |
| Fashion MNIST | 10 | 60 000 / 10 000 | Clothes version of MNIST | torchvision | Yes |
| CIFAR-10 | 10 | 50 000 / 10 000 | Tiny images for classification | torchvision | Yes |
| CIFAR-100 | 100 | 50 000 / 10 000 | Tiny images for classification | torchvision | Yes |
| [Indoor Scene Recognition](http://web.mit.edu/torralba/www/indoor.html) | 67 | 15620 | Dataset for scene classification | -- | Yes |


<!-- ### Multiple labels datasets -->
<!-- 
## Segmentation

| Dataset | Number of classes | Number of samples | Description | Source |
| --- | ---: | ---: | ---: | ---: |
| ADE20k | 10 | 60 000 / 10 000 | General-purpose scene parsing | torchvision | -->