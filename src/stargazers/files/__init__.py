import os
from zlib import crc32

__all__ = [
    "UTF_8_ENCODING",
    "OPEN_MODE",
    "OPEN_MODE_BINARY",
    "READ_MODE",
    "READ_MODE_BINARY",
    "WRITE_MODE",
    "WRITE_MODE_BINARY",
    "to_utf8_bytes",
    "read_utf8_data",
    "write_utf8_data",
    "get_str_hex",
    "get_path_basename_hex",
]


UTF_8_ENCODING = "utf-8"

OPEN_MODE = "rt"
OPEN_MODE_BINARY = "rb"
WRITE_MODE = "wt"
WRITE_MODE_BINARY = "wb"
READ_MODE, READ_MODE_BINARY = OPEN_MODE, OPEN_MODE_BINARY
EXCLUSIVE_MODE = "x"
"""
> `open for exclusive creation, failing if the file already exists`

Use like:
```python
with open(file, mode=WRITE_MODE + EXCLUSIVE_MODE) as f:
    ...
```
"""


_DEFAULT_HASH_MOD = (16**6) - 1


def to_utf8_bytes(to_encode: str):
    return bytes(
        to_encode,
        UTF_8_ENCODING,
    )


def read_utf8_data(file_path: str):
    """
    Opens a byte-encoded file, decodes it to UTF-8 and returns the contents as a string.
    """
    with open(file_path, mode=OPEN_MODE_BINARY) as f:
        return f.read().decode(UTF_8_ENCODING)


def write_utf8_data(file_path: str, data: str):
    """
    Writes a string to a file after encoding it to bytes.
    """
    with open(file_path, WRITE_MODE_BINARY) as f:
        f.write(data.encode(UTF_8_ENCODING))


def get_str_hex(str_var: str, mod_: int = _DEFAULT_HASH_MOD) -> str:
    return f"{hex(crc32(str_var.encode(UTF_8_ENCODING)) % mod_)}"


def get_path_basename_hex(file_path: str, mod_: int = _DEFAULT_HASH_MOD) -> str:
    return get_str_hex(os.path.basename(file_path), mod_)
