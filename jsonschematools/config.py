import os

from dynaconf import Dynaconf

from jsonschematools import ROOT

settings_files = [os.path.join(ROOT, f) for f in ["config.yaml", ".secrets.yaml"]]

settings = Dynaconf(
    envvar_prefix="DYNACONF",  # export envvars with `export DYNACONF_FOO=bar`.
    settings_files=settings_files,  # Load validation in the given order.
)
