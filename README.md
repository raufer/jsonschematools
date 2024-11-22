# JSON Schema Tools

A Python library for working with JSON Schema and OpenAPI specifications, with support for schema resolution and dummy data generation.

## Features

- Resolve JSON Schema references in OpenAPI specifications
- Generate dummy data that conforms to JSON schemas
- Support for schema composition (allOf, anyOf, oneOf)
- Pydantic model compatibility
- Customizable array size and optional field handling

## Installation

Using poetry:

```bash
poetry add jsonschematools
```

Or install from source:

```bash
git clone https://github.com/yourusername/jsonschematools.git
cd jsonschematools
poetry install
```

## Usage

### Schema Resolution

The library can resolve all references in an OpenAPI specification:

```python
from jsonschematools.core.resolve import resolve_openapi_schemas

# Load your OpenAPI spec
with open("openapi.json") as f:
    openapi_spec = json.load(f)

# Resolve all schemas
resolved_schemas = resolve_openapi_schemas(openapi_spec)

# Access a specific resolved schema
question_set_schema = resolved_schemas["QuestionSet-Input"]
```

### Dummy Data Generation

Generate dummy data that conforms to your JSON schemas:

```python
from jsonschematools.core.generate import generate_dummy_data

# Generate dummy data from a schema
dummy_data = generate_dummy_data(schema)

# Generate dummy data for a specific schema from OpenAPI spec
dummy_obj = generate_dummy_object("QuestionSet-Input", openapi_spec)
```

## Development

### Prerequisites

- Python 3.8+
- Poetry

### Setup

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run specific tests
poetry run pytest tests/core/test_generate.py -v
```

### Running Tests

The test suite includes validation of:
- Schema resolution
- Dummy data generation
- Pydantic model integration
- Complex schema handling

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=jsonschematools
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
