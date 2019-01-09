from .mnist import MNIST
from .fashion_mnist import FashionMNIST
from .cifar10 import CIFAR10
from .cifar100 import CIFAR100
from .indoor_scene_recon import IndoorSceneRecon
from .svhn_cropped import SVHN_cropped

__all__ = ['MNIST', 'FashionMNIST', 'CIFAR10', 'CIFAR100', 'IndoorSceneRecon', 'SVHN_cropped']