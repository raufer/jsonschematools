import os
import sys
import pytest

from jsonschematools import ROOT
from jsonschematools.utils.files import read_json

from typing import Any, Generator

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from db,main.py


@pytest.fixture(scope="function")
def schema() -> Generator[dict, Any, None]:
    schema_path = os.path.join(ROOT, "tests/resources/openapi.json")
    data = read_json(schema_path)
    yield data
