# optionaldict

[![Build Status](https://travis-ci.org/messense/optionaldict.svg)](https://travis-ci.org/messense/optionaldict)
[![Coverage Status](https://coveralls.io/repos/messense/optionaldict/badge.svg)](https://coveralls.io/r/messense/optionaldict)

``optionaldict`` is a dict-like object that ignore NoneType values for Python which is pickable and JSON serializable.

# Installation

You can install ``optionaldict`` simply using ``pip``:
```bash
pip install optionaldict
```

# Usage
``optionaldict``'s usage is very simple, you will import it:
```python
from optionaldict import optionaldict
```

then use it just like the built-in ``dict``:

```python
d1 = optionaldict(a=1, b=None)
d1['c'] = 2
d1.setdefault('d', None)

d2 = optionaldict()
d2['a'] = 1
d2['b'] = None
```


