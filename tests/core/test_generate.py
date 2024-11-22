import pytest
from jsonschematools.core.resolve import resolve_openapi_schemas
from jsonschematools.core.generate import generate_dummy_data
from jsonschematools.models.nodes.question_set import QuestionSet
from jsonschematools.models.tasks.credit_report_visualisation import CreditReportVisualisation
from jsonschematools.utils.json import pp


def test_generate_question_set(schema: dict):
    """
    Test that we can:
    1. Resolve the OpenAPI schema
    2. Generate dummy data for QuestionSet
    3. Create a Pydantic QuestionSet model from the dummy data
    """
    # First resolve all schemas
    resolved_schemas = resolve_openapi_schemas(schema)
    assert "QuestionSet-Input" in resolved_schemas
    
    # Get the resolved QuestionSet schema
    question_set_schema = resolved_schemas["QuestionSet-Input"]
    
    # Generate dummy data
    dummy_data = generate_dummy_data(question_set_schema)
    
    question_set = QuestionSet(**dummy_data)
    
    # Verify some basic properties
    assert question_set.type == "QUESTION_SET"
    assert isinstance(question_set.data.questions, list)
    
    # If we have questions, verify their structure
    if question_set.data.questions:
        question = question_set.data.questions[0]
        assert question.id
        assert question.question
        
        # If we have an answer, verify its structure
        if question.answer:
            assert question.answer.id
            assert question.answer.answer
            assert isinstance(question.answer.references, list)
            
            # If we have references, verify their structure
            if question.answer.references:
                ref = question.answer.references[0]
                assert ref.document_id


def test_generate_credit_report_visualisation(schema: dict):
    """
    Test that we can:
    1. Resolve the OpenAPI schema
    2. Generate dummy data for CreditReportVisualisation
    3. Create a Pydantic CreditReportVisualisation model from the dummy data
    """
    # First resolve all schemas
    resolved_schemas = resolve_openapi_schemas(schema)
    assert "CreditReportVisualisation-Input" in resolved_schemas
    
    # Get the resolved CreditReportVisualisation schema
    vis_schema = resolved_schemas["CreditReportVisualisation-Input"]
    
    # Generate dummy data
    dummy_data = generate_dummy_data(vis_schema)
    
    # Create Pydantic model from dummy data
    visualisation = CreditReportVisualisation(**dummy_data)
    
    # Verify basic properties
    assert visualisation.type == "CREDIT_REPORT_VISUALISATION"
    
    # Verify data structure if present
    if visualisation.data:
        assert isinstance(visualisation.data.visualisations, list)
        
        # If we have visualisations, verify their structure
        if visualisation.data.visualisations:
            vis = visualisation.data.visualisations[0]
            assert vis.title
            assert vis.description
            assert vis.type == "LINE_PLOT"
            
            # Verify visualisation data
            assert isinstance(vis.data.x_values, list)
            assert isinstance(vis.data.series, list)
            
            # If we have series, verify their structure
            if vis.data.series:
                series = vis.data.series[0]
                assert series.name
                assert isinstance(series.y_values, list)
