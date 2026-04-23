# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - YYYY-MM-DD

## [0.1.0] - 2022-11-24

### Added

- DefineIf class implemented, we can now use it via inheritance and decorators. For
  example:

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
