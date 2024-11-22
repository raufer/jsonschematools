from typing import Any, Optional


def clean_llm_values(x: Any) -> Optional[str]:
    """Clean the values of the LLM outputs

    * The model sometimes outputs <UNKNOWN> instead of the requested None
    """
    if isinstance(x, str) and "unknown" in x.lower():
        return None

    return x
