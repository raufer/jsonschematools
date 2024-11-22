import jsonschema
from jsonschematools.core.resolve import resolve_openapi_schemas
from jsonschematools.utils.json import pp


def test_resolve(schema: dict):
    resolved = resolve_openapi_schemas(schema)
    assert len(resolved) == 85
    pp(resolved["ConditionalInvestigation-Output"])
    raise
    assert "ConditionalInvestigationData-Output" in resolved
