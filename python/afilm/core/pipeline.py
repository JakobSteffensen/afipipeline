# ----------------------------------------------------------------------------------------------------------------------
# file       : afilm.core.pipelie
# created    : 23/05/2023
# email      : js@anim.dk
#
#
# ----------------------------------------------------------------------------------------------------------------------
from pathlib import Path


def pipeline_root():
    """ Return the path to the root of the pipeline."""
    root = '\\'.join(__file__.split('\\')[0:-4])
    return Path(root)


def python_root():
    """ Return the path to the root of the pipeline."""
    root = '\\'.join(__file__.split('\\')[0:-3])
    return Path(root)