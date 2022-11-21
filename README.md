# Define If

**If the condition is true, define the method.**

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hakancelikdev/defineif/main.svg)](https://results.pre-commit.ci/latest/github/hakancelikdev/defineif/main)
[![test](https://github.com/hakancelikdev/defineif/actions/workflows/tests.yml/badge.svg)](https://github.com/hakancelikdev/defineif/actions/workflows/tests.yml)
[![build-docs](https://github.com/hakancelikdev/defineif/actions/workflows/docs.yml/badge.svg)](https://github.com/hakancelikdev/defineif/actions/workflows/docs.yml)
[![publish-package-on-pypi](https://github.com/hakancelikdev/defineif/actions/workflows/pypi.yml/badge.svg)](https://github.com/hakancelikdev/defineif/actions/workflows/pypi.yml)

[![Pypi](https://img.shields.io/pypi/v/defineif)](https://pypi.org/project/defineif/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/defineif)
[![Downloads](https://static.pepy.tech/personalized-badge/defineif?period=total&units=international_system&left_color=grey&right_color=red&left_text=downloads)](https://pepy.tech/project/defineif)
[![License](https://img.shields.io/github/license/hakancelikdev/defineif.svg)](https://github.com/hakancelikdev/defineif/blob/main/LICENSE)

[![Forks](https://img.shields.io/github/forks/hakancelikdev/defineif)](https://github.com/hakancelikdev/defineif/fork)
[![Issues](https://img.shields.io/github/issues/hakancelikdev/defineif)](https://github.com/hakancelikdev/defineif/issues)
[![Stars](https://img.shields.io/github/stars/hakancelikdev/defineif)](https://github.com/hakancelikdev/defineif/stargazers)

[![Codecov](https://codecov.io/gh/hakancelikdev/defineif/branch/main/graph/badge.svg)](https://codecov.io/gh/hakancelikdev/defineif)
[![Contributors](https://img.shields.io/github/contributors/hakancelikdev/defineif)](https://github.com/hakancelikdev/defineif/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/hakancelikdev/defineif.svg)](https://github.com/hakancelikdev/defineif/commits/main)

For more information see: https://defineif.hakancelik.dev/

## How to install ?

```
pip install defineif
```

## How to use it ?

```python
import os

from defineif import DefineIf


class Klass(DefineIf):

    @staticmethod
    @DefineIf(os.name == 'nt')
    def get_platform():
        return 'Windows'

    @staticmethod
    @DefineIf(os.name == 'posix')
    def get_platform():
        return 'Linux'

platform = Klass.get_platform()

print(platform)
```
