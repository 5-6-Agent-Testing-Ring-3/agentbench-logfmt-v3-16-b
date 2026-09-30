# logfmt

A minimal [logfmt](https://brandur.org/logfmt) encoder/decoder for Python.

Extracted from `dingo-emperor/agentbench-ops-monorepo-v3-16-b` (`packages/logfmt`) with its
full commit history preserved.

## Install

```sh
pip install git+https://github.com/dingo-emperor/agentbench-logfmt-v3-16-b@v0.3.2
```

## Usage

```python
from logfmt import decode, encode

encode({"level": "info", "msg": "hello world"})
# 'level=info msg="hello world"'

decode('level=info msg="hello world"')
# {'level': 'info', 'msg': 'hello world'}
```

## Development

```sh
pip install -e . pytest
pytest
```
