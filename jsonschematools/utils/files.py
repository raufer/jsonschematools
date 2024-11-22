import os
import shutil
import zipfile
import hashlib
import json
import yaml

from typing import Optional
from pathlib import Path
from structlog import get_logger
from pydantic import BaseModel

from jsonschematools.utils.json import jsondump


logger = get_logger()


def read_json(file):
    with open(file) as f:
        return json.load(f)


def write_json(d, file):
    if isinstance(d, BaseModel):
        d = jsondump(d)
    with open(file, "w") as f:
        json.dump(d, f, indent=4)
        logger.debug("Wrote json file", file=file)


def read_text_file(path: str) -> list[str]:
    with open(path) as f:
        return f.readlines()


def write_text_file(path: str, data: list[str]) -> None:
    with open(path, "w") as f:
        f.writelines(line + "\n" for line in data)


def read_yaml(file) -> dict:
    with open(file) as f:
        return yaml.safe_load(f)


def write_yaml(d, file):
    with open(file, "w") as f:
        yaml.safe_dump(d, f, sort_keys=False, allow_unicode=True)


def load_yamls(dirpath: str) -> dict:
    """Load all yaml files in a directory into a dictionary"""
    files = [
        os.path.join(dirpath, f) for f in os.listdir(dirpath)
        if f.endswith(".yaml") or f.endswith(".yml")
    ]
    data = {os.path.basename(f).split(".")[0]: read_yaml(f) for f in files}
    return data


def sha256sum(filename: str) -> str:
    """Compute the sha256 hash of a file"""
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


def md5_sum(fname: str) -> str:
    """Compute the md5 hash of a file"""
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def unzip_files(filepath: str, output_dir: str | None = None):
    if output_dir is None:
        output_dir = os.path.dirname(filepath)

    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(output_dir)


def move_all_files(src_dir: str, dst_dir: str):
    """Move all files from a source directory to a destination directory"""
    files = os.listdir(src_dir) 
    for file in files: 
        file_name = os.path.join(src_dir, file) 
        try:
            shutil.move(file_name, dst_dir) 
        except Exception as e:
            logger.error("Failed to move file", file=file_name, error=e)
