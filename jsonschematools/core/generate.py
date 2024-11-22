from typing import Any, Dict, List
from copy import deepcopy
from .resolve import resolve_openapi_schemas, merge_schemas


def generate_dummy_data(schema: Dict[str, Any]) -> Any:
    """
    Generates dummy data that conforms to the given JSON schema.
    Always populates optional fields and includes one element for arrays.
    
    Args:
        schema: The JSON schema to generate data for
        
    Returns:
        Any: Generated dummy data matching the schema
    """
    if not isinstance(schema, dict):
        return schema
        
    # Handle anyOf/oneOf by taking first option
    if "anyOf" in schema:
        return generate_dummy_data(schema["anyOf"][0])
    if "oneOf" in schema:
        return generate_dummy_data(schema["oneOf"][0])
        
    # Handle different types
    schema_type = schema.get("type")
    
    if schema_type == "object":
        result = {}
        properties = schema.get("properties", {})
        
        for prop_name, prop_schema in properties.items():
            result[prop_name] = generate_dummy_data(prop_schema)
            
        # Handle default values
        if "default" in schema:
            result.update(schema["default"])
            
        return result
        
    elif schema_type == "array":
        # Always include exactly one item
        items_schema = schema.get("items", {})
        return [generate_dummy_data(items_schema)]
        
    elif schema_type == "string":
        if "enum" in schema:
            return schema["enum"][0]
        if "const" in schema:
            return schema["const"]
        return f"dummy_{schema.get('title', 'string')}"
        
    elif schema_type == "number":
        if "minimum" in schema:
            return schema["minimum"]
        return 0.0
        
    elif schema_type == "integer":
        if "minimum" in schema:
            return schema["minimum"]
        return 0
        
    elif schema_type == "boolean":
        return schema.get("default", True)
        
    elif schema_type == "null":
        return None
        
    # Handle composition
    if "allOf" in schema:
        merged = merge_schemas([generate_dummy_data(s) for s in schema["allOf"]])
        return generate_dummy_data(merged)
        
    return None


def generate_dummy_object(schema_name: str, openapi_spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a dummy object for a named schema from an OpenAPI specification.
    
    Args:
        schema_name: Name of the schema to generate data for
        openapi_spec: Complete OpenAPI specification
        
    Returns:
        Dict[str, Any]: Generated dummy object
        
    Raises:
        ValueError: If schema_name is not found in OpenAPI spec
    """
    # First resolve the schema
    resolved_schemas = resolve_openapi_schemas(openapi_spec)
    if schema_name not in resolved_schemas:
        raise ValueError(f"Schema {schema_name} not found in OpenAPI spec")
        
    # Generate dummy data from resolved schema
    return generate_dummy_data(resolved_schemas[schema_name])