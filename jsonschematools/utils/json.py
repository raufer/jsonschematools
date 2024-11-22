import json
import re

import orjson
from pydantic import BaseModel
from pydantic.v1 import BaseModel as BaseModelV1

from jsonschematools.ops.dicts import f_map
from jsonschematools.utils.llm import clean_llm_values


def jsondump(obj: BaseModel | BaseModelV1 | dict | list) -> dict:
    if isinstance(obj, dict):
        return obj
    elif isinstance(obj, list):
        return [jsondump(o) for o in obj]
    elif isinstance(obj, BaseModelV1):
        return orjson.loads(obj.json(by_alias=True))
    else:
        return orjson.loads(obj.model_dump_json(by_alias=True)) 


def pp(d) -> None:
    d = jsondump(d)
    print(json.dumps(d, indent=2))
