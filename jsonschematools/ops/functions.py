import inspect


def signature_args(f) -> dict:
    """Return the signature of a function."""
    sig = inspect.signature(f)

    args = {}
    for param in sig.parameters.values():
        if param.annotation == inspect._empty:
            raise TypeError(f"Missing type annotation for {param.name}")

        args[param.name] = param.annotation

    return args


def identity(x):
    return x

