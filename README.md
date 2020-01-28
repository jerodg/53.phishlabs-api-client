```

```
![platform](https://img.shields.io/badge/Platform-Mac/*nix/Windows-blue.svg)
![python](https://img.shields.io/badge/Python-8%2B-blue.svg)
![bricata](https://img.shields.io/badge/Phishlabs-blue.svg)
<a href="https://www.mongodb.com/licensing/server-side-public-license"><img src="https://img.shields.io/badge/License-SSPL-green.svg"></a>
![0%](https://img.shields.io/badge/Coverage-0%25-red.svg)
<a href="https://saythanks.io/to/jerodg"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a>


Phishlabs API Client


## Installation
```bash
pip install phishlabs-api-client
```

## Basic Usage
Works with Phishlabs API

*See examples folder for more*

### Class Inheritence
```python
from phishlabs_api_client import PhishlabsApiClient

class MyClass(PhishlabsApiClient):
    def __init__(self):
        PhishlabsApiClient.__init__(self, cfg='/path/to/config.toml')
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        PhishlabsApiClient.__aexit__(self, exc_type, exc_val, exc_tb)
```

### Context Manager
```python
from phishlabs_api_client import PhishlabsApiClient

async with PhishlabsApiClient(cfg='/path/to/config.toml') as bac:
    alerts = bac.get_alerts()
```

## Documentation
[GitHub Pages](https://jerodg.github.io/phishlabs-api-client/)
- Work in Process

## API Implementation, Categories (0/2) ~0%, Functions (0/6) ~0%

- [ ] Cases
    - [ ] Get All Cases
    - [ ] Get All Cases Filtered
    - [ ] Get One Case
    - [ ] Get All Cases Count
    - [ ] Get All Cases Count Filtered
- [ ] Attachments
    - [ ] Get One Cases Attachments


## License
Copyright © 2019 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
