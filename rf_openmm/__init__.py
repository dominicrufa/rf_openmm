"""
rf_openmm
a library and implementation sandbox for the reaction field nonbonded method in OpenMM
"""

# Add imports here
from .rf_openmm import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
