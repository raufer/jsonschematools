import os
import inspect

from glob import glob
from functools import cache
from structlog import get_logger

from dotmap import DotMap

from jsonschematools.utils.files import load_yamls
from jsonschematools import ROOT
from jsonschematools.config import settings


logger = get_logger()


def load_local_repository(repodir: str) -> dict:
    """Loads all prompts from local repository"""
    repository_path = os.path.join(ROOT, repodir)

    files = glob(os.path.join(repository_path, "**/*.yaml"), recursive=True)
    if not files:
        raise FileNotFoundError(f"No files found in {repository_path}")

    logger.debug("Loading local repository", repodir=repodir, num_files=len(files))
    
    def loop(dir):
        blobs = [os.path.join(dir, f) for f in os.listdir(dir)]
        dirs = [f for f in blobs if os.path.isdir(f)]

        local_files = load_yamls(dir)
        entries = [{os.path.basename(d): loop(d) for d in dirs}] + [local_files]

        data = {}
        for entry in entries:
            data.update(entry)

        return data

    data = loop(repository_path)
    return data


@cache
def local_domain_repository() -> dict:
    """Loads domain context information
    Contains context about the operating domain and the various tasks
    Returns an object supporting dot notation for attribute access
    """
    domain = load_local_repository(settings.local.domain_repository)
    # print(DotMap(domain, _dynamic=False)['context']['checks']['check_5'].keys())
    return DotMap(domain, _dynamic=False)

