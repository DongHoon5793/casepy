# casepy

[![Documentation
Status](https://readthedocs.org/projects/casepy/badge/?version=latest)](http://casepy.readthedocs.io/?badge=latest)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI download
total](https://img.shields.io/pypi/dm/casepy.svg)](https://pypi.org/project/casepy/)
[![GitHub
license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

**casepy** is a Python package for the advanced case combination and
permutation calculation.

This package is designed to be possible to calculation of the case
combination and permutation from the duplicated elements.

This package is designed to calculate combinations and permutations from
the duplicate elements list. You can designate the number of elements
you want to select. For instance, you can get all combinations and
permutations of choosing 5 elements in a given list \[1,1,2,3,4,5,5\].

The combination and permutation list is sorted by numerical or
alphabetical. Using the n-th-permutation or n-th-combination, you can
get the n-th permutation or n-th combination of a given parameter
without calculating 0-th to (n-1)-th case (current method).

Documentation: [![Documentation
Status](https://readthedocs.org/projects/casepy/badge/?version=latest)](http://casepy.readthedocs.io/?badge=latest)

## Installation

You can install casepy via pip from PyPI:

``` console
$ pip install casepy
```

## Quick Start

``` python
import casepy

element_list = [1, 2, 2, 3, 4]

all_combinations = casepy.all_combinations(element_list, 2)
# [[1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [2, 4], [3, 4]]

all_permutations = casepy.all_permutations(test_list, 2)
# [[1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
```