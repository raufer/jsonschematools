from typing import Any, Dict, Union, List
from copy import deepcopy
from jsonschematools.utils.json import pp


def merge_schemas(schemas: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merges multiple schemas into one, handling properties and requirements.
    
    Args:
        schemas: List of schemas to merge
        
    Returns:
        Dict[str, Any]: Merged schema
    """
    merged = {}
    properties = {}
    required = set()
    
    for schema in schemas:
        # Merge properties
        if "properties" in schema:
            properties.update(schema.get("properties", {}))
            
        # Merge required fields
        if "required" in schema:
            required.update(schema.get("required", []))
            
        # Copy other fields if not already present
        for key, value in schema.items():
            if key not in ["properties", "required"]:
                merged[key] = value
    
    if properties:
        merged["properties"] = properties
    if required:
        merged["required"] = sorted(list(required))
        
    return merged


def resolve_schema(schema: Dict[str, Any], root_schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively resolves all $ref references in a JSON Schema by replacing them with their full definitions.
    
    Args:
        schema: The schema object or subschema to resolve
        root_schema: The root schema containing all definitions
        
    Returns:
        Dict[str, Any]: The fully resolved schema with all references replaced
    """
    if not isinstance(schema, (dict, list)):
        return schema

    if isinstance(schema, list):
        return [resolve_schema(item, root_schema) for item in schema]

    resolved = {}
    
    # Handle composition keywords
    if "allOf" in schema:
        sub_schemas = [resolve_schema(s, root_schema) for s in schema["allOf"]]
        base_schema = {k: v for k, v in schema.items() if k != "allOf"}
        return merge_schemas([base_schema] + sub_schemas)
        
    if "anyOf" in schema:
        schema["anyOf"] = [resolve_schema(s, root_schema) for s in schema["anyOf"]]
        return schema
        
    if "oneOf" in schema:
        schema["oneOf"] = [resolve_schema(s, root_schema) for s in schema["oneOf"]]
        return schema
    
    for key, value in schema.items():
        if key == "$ref":
            # Handle reference resolution
            ref_path = value.split("/")[1:]  # Split "#/components/schemas/X" into parts
            ref_schema = root_schema
            
            # Navigate to the referenced schema
            for path_part in ref_path:
                ref_schema = ref_schema[path_part]
            
            # Recursively resolve any refs in the referenced schema
            resolved_ref = resolve_schema(deepcopy(ref_schema), root_schema)
            
            # Merge with any additional properties in the original schema
            base_schema = {k: v for k, v in schema.items() if k != "$ref"}
            if base_schema:
                return merge_schemas([base_schema, resolved_ref])
            return resolved_ref
        
        elif isinstance(value, dict):
            resolved[key] = resolve_schema(value, root_schema)
        elif isinstance(value, list):
            resolved[key] = [resolve_schema(item, root_schema) for item in value]
        else:
            resolved[key] = value
            
    return resolved


def resolve_openapi_schemas(openapi_spec: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Resolves all schema definitions in an OpenAPI specification by replacing $ref references
    with their full definitions.
    
    Args:
        openapi_spec: The complete OpenAPI specification
        
    Returns:
        Dict[str, Dict[str, Any]]: A dictionary of fully resolved schema definitions
    """
    schemas = openapi_spec.get("components", {}).get("schemas", {})
    resolved_schemas = {}
    
    # Resolve each schema definition
    for schema_name, schema in schemas.items():
        resolved_schemas[schema_name] = resolve_schema(deepcopy(schema), openapi_spec)
        
    return resolved_schemas
