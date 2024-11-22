def get_null_entry_for(class_):
    """Get a null entry for a given class"""
    fields = class_.__fields__
    return {k: None for k in fields.keys()}