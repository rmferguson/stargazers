import os
import typing
from json import dumps, load
from zipfile import ZipFile
from zlib import crc32

from .sg_classes import AbstractContextManager

__all__ = [
    "UTF_8_ENCODING",
    "OPEN_MODE",
    "OPEN_MODE_BINARY",
    "READ_MODE",
    "READ_MODE_BINARY",
    "WRITE_MODE",
    "WRITE_MODE_BINARY",
    "JSON_EXT",
    "DOT_JSON",
    "DEFAULT_HASH_MOD",
    "JSONIndentConsts",
    "JSONFileUpdateHandler",
    "to_utf8_bytes",
    "read_utf8_data",
    "write_utf8_data",
    "read_utf8_json_data",
    "write_utf8_json_data",
    "get_str_hex",
    "get_path_basename_hex",
    "squish_json",
]


UTF_8_ENCODING = "utf-8"

OPEN_MODE = "r"
OPEN_MODE_BINARY = "rb"
READ_MODE, READ_MODE_BINARY = OPEN_MODE, OPEN_MODE_BINARY
WRITE_MODE = "w"
WRITE_MODE_BINARY = "wb"

JSON_EXT = "json"  # Prefer this one.
DOT_JSON = ".json"


class JSONIndentConsts(object):
    STANDARD = 2 if __debug__ else None
    SPARSE = 4
    LOOSE = 2
    TIGHT = None


DEFAULT_HASH_MOD = (16**6) - 1


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


def read_utf8_json_data(file_path: str):
    """
    Opens a file containing JSON data, closes it, and returns the contents as a JSON object.
    """
    with open(file_path, OPEN_MODE, encoding=UTF_8_ENCODING) as json_data:
        return load(json_data)


def write_utf8_json_data(
    file_path: str,
    json_data: typing.Any,  # Fuck it, you know what JSON data looks like.
    indent: typing.Union[int, None] = JSONIndentConsts.LOOSE,
    sort_keys=False,
):
    """
    Writes valid JSON to a file after converting it to a string representation.
    """
    data = dumps(json_data, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
    write_utf8_data(file_path, data)


def get_str_hex(str_var: str, _mod: int = DEFAULT_HASH_MOD) -> str:
    return f"{hex(crc32(str_var.encode(UTF_8_ENCODING)) % _mod):6}"


def get_path_basename_hex(file_path: str, _mod: int = DEFAULT_HASH_MOD) -> str:
    return get_str_hex(os.path.basename(file_path), _mod)


def squish_json(json_data: typing.Union[typing.Dict, typing.List]) -> str:
    """
    Formats JSON data to the tightest possible representation in str form.
    """
    return dumps(json_data, indent=None, separators=(",", ":"))


# TODO(@Robert): write a file after compressing the data.
# Probably convert the data to bytes and compress that?


# TODO(@Robert): Doesn't seem to quite work right?
def zip_directory(target_directory: str):
    with ZipFile(f"{target_directory}.zip", mode="w") as data_backup:
        for _, subdirectory, files in os.walk(target_directory):
            for sub in subdirectory:
                for file in files:
                    original = os.path.join(target_directory, sub, file)
                    data_backup.write(filename=original, arcname=file)


class JSONFileUpdateHandler(AbstractContextManager):
    """
    When used as a context manager:
    1. Opens, reads and closes a JSON file.
    2. Can receive updates to the .data attribute
    3. Opens, writes, and closes the same JSON file with the contents of .data

    This class will fail (intentionally!) if the file does not exist.
    """

    def __init__(self, file_path: str, indentation=JSONIndentConsts.STANDARD):
        self.file_path = file_path
        self.data = read_utf8_json_data(file_path)
        self.indentation = indentation

    def __enter__(self):
        return self

    def __exit__(self, typ, val, tb):
        write_utf8_json_data(self.file_path, self.data, indent=self.indentation)
