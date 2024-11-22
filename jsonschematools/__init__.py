import logging.config
import os
import sys
import time
from pathlib import Path

import structlog

from jsonschematools.utils.infra import is_notebook


shared_processors = [
    # Processors that have nothing to do with output,
    # e.g., add timestamps or log level names.
    structlog.contextvars.merge_contextvars,
    structlog.processors.add_log_level,
    structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S"),
    structlog.processors.StackInfoRenderer(),
]

if sys.stderr.isatty() or is_notebook():
    # Pretty printing when we run in a terminal session.
    # Automatically prints pretty tracebacks when "rich" is installed
    processors = shared_processors + [
        structlog.dev.ConsoleRenderer(
            exception_formatter=structlog.dev.rich_traceback, colors=True
        ),
        structlog.dev.set_exc_info,
    ]

else:
    processors = shared_processors + [
        structlog.dev.ConsoleRenderer(
            exception_formatter=structlog.dev.rich_traceback, colors=True
        ),
        structlog.dev.set_exc_info,
    ]
    # Print JSON when we run, e.g., in a Docker container.
    # Also print structured tracebacks.
    # processors = shared_processors + [
    #     structlog.processors.dict_tracebacks,
    #     structlog.processors.JSONRenderer(),
    # ]

ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
timestr = time.strftime("%Y%m%d-%H%M%S")

structlog.configure(
    processors=processors,
    wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
    cache_logger_on_first_use=False,
)


